##NuPhylo: A tool for creating NCLDV marker gene trees

import pandas as pd
import sys,argparse,os,re,subprocess


argparser = argparse.ArgumentParser(description = 'NuPhylo: A tool for creating NCLDV marker gene trees')
argparser.add_argument('-i', '--input', help = 'Input protein sequences', required = True)
argparser.add_argument('-o', '--output', help = 'Output directory', required = True)
argparser.add_argument('-m', '--marker', help = 'Marker gene', required = True, choices = ['MCP', 'A32', 'PolB', 'RNAPL', 'RNAPS', 'SF2', 'TF2B', 'Topo2', 'VLTF3'])

args = argparser.parse_args()

input = args.input
output = args.output
marker = args.marker

if not os.path.exists(output):
    os.mkdir(output)


##Check which marker gene

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

##Make a tree
print('Making tree')
fasttree= 'fasttree '+ output + '/allseqs.aln > ' + output + '/allseqs.nwk'
subprocess.call(fasttree, shell=True)

