##NuPhylo: A tool for creating NCLDV marker gene trees

import pandas as pd
import sys,argparse,os,re,subprocess


argparser = argparse.ArgumentParser(description = 'NuPhylo: A tool for creating NCLDV marker gene trees')
argparser.add_argument('-i', '--input', help = 'Input protein sequences, can be multiple separated by a comma for concat mode (make sure they are same order as marker selections)', required = True)
argparser.add_argument('-o', '--output', help = 'Output directory', required = True)
argparser.add_argument('-m', '--marker', help = 'Marker gene, can choose multiple separated by comma if doing concat mode', required = True)
argparser.add_argument('-cat', '--concat', help = 'Concatinated Alignment', required = False, action='store_true')
#add a flag which if present will change to extended mode
argparser.add_argument('-e', '--extended', help = 'Extended phylogeny with animals, bacteria, fungi, plants, and archaea (only avaliable for some genes)', required = False, action='store_true')
args = argparser.parse_args()

input = args.input
output = args.output
marker = args.marker
extended = args.extended
concat = args.concat
if not os.path.exists(output):
    os.mkdir(output)
if concat==True:
    #get list of markers, separate by commas
    markers= marker.split(',')
    inputs= input.split(',')
    for marker in markers:
        markerfile= 'Markers/' + marker + '.final.faa'
        inputfile= inputs[markers.index(marker)]
        #cat
        cat= 'cat ' + inputfile + ' ' + markerfile + ' > ' + output + '/'+marker+'_allseqs.faa'
        subprocess.call(cat, shell=True)
        #mafft
        mafft= 'mafft --auto ' + output + '/'+marker+'_allseqs.faa > ' + output + '/'+marker+'_allseqs.aln'
        subprocess.call(mafft, shell=True)
        #trimal
        trimal= 'trimal -in ' + output + '/'+marker+'_allseqs.aln -out ' + output + '/'+marker+'_allseqs.trimmed.aln -gt 0.1'
        subprocess.call(trimal, shell=True)
    #Concatinate all trimmed alignments
    conncat= 'catfasta2phyml -f --intersect '+output+'/*.trimmed.aln'+' > '+output+'/Concatinated.aln'
    subprocess.call(conncat, shell=True)
    #Make a tree
    fasttree= 'fasttree '+ output + '/Concatinated.aln > ' + output + '/Concatinated_tree.nwk'
    subprocess.call(fasttree, shell=True)

else:
    ##Check which marker gene
    #check if extended mode is on
    if extended == True:
        if marker == 'MCP':
            markerfile= 'Markers/MCP.final.faa'
        elif marker == 'A32':
            markerfile= 'Markers/A32.final.faa'
        elif marker == 'PolB':
            markerfile= 'Markers/PolBextended.final.faa'
        elif marker == 'RNAPL':
            markerfile= 'Markers/RNAPLextended.final.faa'
        elif marker == 'RNAPS':
            markerfile= 'Markers/RNAPSextended.final.faa'
        elif marker == 'SF2':
            markerfile= 'Markers/SF2.final.faa'
        elif marker == 'TF2B':
            markerfile= 'Markers/TF2Bextended.final.faa'
        elif marker == 'Topo2':
            markerfile= 'Markers/Topo2extended.final.faa'
        elif marker == 'VLTF3':
            markerfile= 'Markers/VLTF3.final.faa'
        else:
            print('Error: Invalid Marker gene selected')
            sys.exit()
    else:
        if marker == 'MCP':
            markerfile= 'Markers/MCP.final.faa'
        elif marker == 'A32':
            markerfile= 'Markers/A32.final.faa'
        elif marker == 'PolB':
            markerfile= 'Markers/PolB.final.faa'
        elif marker == 'RNAPL':
            markerfile= 'Markers/RNAPL.final.faa'
        elif marker == 'RNAPS':
            markerfile= 'Markers/RNAPS.final.faa'
        elif marker == 'SF2':
            markerfile= 'Markers/SF2.final.faa'
        elif marker == 'TF2B':
            markerfile= 'Markers/TF2B.final.faa'
        elif marker == 'Topo2':
            markerfile= 'Markers/Topo2.final.faa'
        elif marker == 'VLTF3':
            markerfile= 'Markers/VLTF3.final.faa'
        else:
            print('Error: Invalid Marker gene selected')
            sys.exit()
    ##DO an alignment

    print('Aligning sequences')
    cat= 'cat ' + input + ' ' + markerfile + ' > ' + output + '/allseqs.faa'
    subprocess.call(cat, shell=True)
    mafft= 'mafft --auto ' + output + '/allseqs.faa > ' + output + '/allseqs.aln'
    subprocess.call(mafft, shell=True)

    ##Trim the alignment
    trimal= 'trimal -in ' + output + '/allseqs.aln -out ' + output + '/allseqs.trimmed.aln -gt 0.1'
    subprocess.call(trimal, shell=True)

    ##Make a tree
    print('Making tree')
    fasttree= 'fasttree '+ output + '/allseqs.trimmed.aln > ' + output + '/allseqs.nwk'
    subprocess.call(fasttree, shell=True)

