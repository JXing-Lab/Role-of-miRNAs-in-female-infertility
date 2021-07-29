import csv


def append_gnomad(file_dict,gnomad_dict,is_mirna_file):
    """
    Used to append gnomAD information to the provided file_dict.

    Merges Allele Counts and Allele Numbers.

    Parameters:
    file_dict(dict): A dictionary from mirvas_reformatter, admire_reformatter, or utr_reformatter output
    gnomad_dict(dict): A dictionary containing gnomAD annotations from gnomad_reformatter output
    is_mirna_file(boolean): True indicates the file_dict follows mirvas_reformatter or admire_reformatter output. False assumes the output comes from utr_reformatter.

    Returns: 
    appended_dict(dict): A dictionary with gnomAD data appended.
    """
    appended_dict = dict()

    for keys in file_dict.keys():
        value = file_dict[keys]
        line = value.split('\t')

        if(is_mirna_file):
            #Chr,Start,End,Ref,Alt
            pos = line[0]+line[1]+line[2]+line[3]+line[4]
            #DBSNP150
            rs_num = line[18]
            #AC_LRG+AC_HRG
            ac_patient=int(line[11]) + int(line[14])
            #AN_LRG+AN_HRG
            an_patient=int(line[12]) + int(line[15])
            af_patient = ac_patient/an_patient if an_patient else 0
        else:
            #Chr,Start,End,Ref,Alt
            pos = line[0]+line[1]+line[2]+line[4]+line[5]

            #DBSNP150
            rs_num = line[13]
            #AC_LRG+AC_HRG
            ac_patient=int(line[6]) + int(line[9])
            #AN_LRG+AN_HRG
            an_patient=int(line[7]) + int(line[10])
            af_patient = ac_patient/an_patient if an_patient else 0

        if rs_num in gnomad_dict:
            gnomad_data = gnomad_dict[rs_num]
        elif pos in gnomad_dict:
            gnomad_data = gnomad_dict[pos]
        else:
            gnomad_data = '\t'.join(['-','-','-'])
        if(is_mirna_file):
            #Chr    Start   End Ref Alt miRNA   Type    Location    PredictedEffect_Centroid    PredictedEffect_MEA PredictedEffect_MFE AC_LRG  AN_LRG  AF_LRG  AC_HRG  AN_HRG  AF_HRG  DBSNP135    DBSNP150
            append_line = '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],str(ac_patient),str(an_patient),str(af_patient),gnomad_data,line[17],line[18]])
        else:
            #Chr  Start   End Gene    Ref Alt AC_Patient  AN_Patient  AF_Patient  AC_NFE  AN_NFE  AF_NFE  DBSNP135    DBSNP150
            append_line = '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],str(ac_patient),str(an_patient),str(af_patient),gnomad_data,line[12],line[13]])

        appended_dict[keys] = append_line

    return appended_dict

def append_is_expressed(input_dict, expressed_list, full_list):
    """
    Appends YES to row if found in expressed list, NO to row if not found in expressed list but found in full list, NA otherwise.

    Parameters:
    input_dict(dict): Dictionary with variant file information.
    expresssed_list(string): Path to list of genes that are expressed.
    full_list(string): Path to list full list of genes found in the study.

    Returns:
    output_dict(dict): Dictionary with is_Expression Appended
    """
    if(expressed_list == None or full_list == None):
        return None
    genes_list = set(line.strip() for line in open(full_list))
    expressed = set(line.strip() for line in open(expressed_list))
    output_dict = dict()
    for key in input_dict.keys():
        column = input_dict[key].split('\t')
        g = column[3]
        genes = g.split(';')
        isExp = 0
        isNonExp = 0
        for gene in genes:
            if(gene in expressed):
                isExp = 1
            elif(gene in genes_list):
                isNonExp = 1
        if(isExp == 1):
            column.append('YES')
            append_line = '\t'.join(column)
        elif(isNonExp == 1):
            column.append('NO')
            append_line = '\t'.join(column)
        else:
            column.append('NA')
            append_line = '\t'.join(column)
        output_dict[key] = append_line

    return output_dict

def merge_dict(mirvas_dict,admire_dict):
    """
    Merges miRVaS and ADmiRE dictionaries together.

    miRVaS annotations take precedence over ADmiRE annotations. 
    If ADmiRE identifies a seed region that miRVaS does not, label the region as seed.

    Parameters:
    mirvas_dict(dict): The miRVaS dictionary constructed by mirvas_reformatters.py
    admire_dict(dict): The ADmiRE dictionary constructed by admire_reformatters.py

    Returns:
    mreged_dict(dict): A merged dictionary with all variants found in both mirvas_dict and admire_dict.
    """
    merged_dict = dict()
    print("Merging Dictionaries")
    for key in mirvas_dict.keys():
        if key in admire_dict.keys():
            mirvas_line = mirvas_dict[key].split('\t')
            admire_line = admire_dict[key].split('\t')
            location_mirvas = mirvas_line[7]
            location_admire = admire_line[7]
            if(location_mirvas != 'seed' and location_admire == 'seed'):
                #Replace location_mirvas with location_admire.  Everything else remains the same.
                merged_dict[key] = mirvas_dict[key].replace(location_mirvas,location_admire)
            else:
                merged_dict[key] = mirvas_dict[key]
        else:
            merged_dict[key] = mirvas_dict[key]
    
    for key in admire_dict.keys():
        if key not in merged_dict.keys():
            merged_dict[key] = admire_dict[key]

    return merged_dict

def write_dictionary_to_file(input_dict,output_file,header):
    """
    Writes dictionary to output_file.
    """
    try:
        print("Writing to %s" % output_file)
        with open(output_file, 'w') as file:
            file.write('\t'.join(header) + '\n')
           
            for key in input_dict.keys():
                file.write(input_dict[key]+ '\n')
    except IOError:
        print("I/O error")