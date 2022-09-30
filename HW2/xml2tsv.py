import sys
from lxml import etree
from collections import defaultdict

def main():
    args = sys.argv
    fsimage_xml = args[1]
    inode_directory_list = [] #Adjacency list for directories
    directory_content_map = {} #map of directory number with the related content

    ad_list_test = {'16385': ['16386'], '16386': ['16387', '16391'], '16387': ['16390', '16388'], '16391': ['16392'], '16392': ['16394'], '16390':[],'16388':[],'16394':[]}
    # fsimage_tsv = args[2]

    fsimage_tree = etree.parse(open(fsimage_xml))
    inode_directory = fsimage_tree.xpath('/fsimage/INodeDirectorySection/*')
    inode_section = fsimage_tree.xpath('/fsimage/INodeSection/*')

    # print('test>>',inode_directory[0][0].tag)
    #Create Adjacency list according to the inode directory structure
    inode_directory_list = create_inode_directory_structure(inode_directory)


    #Create a map of directory number with the related content
    directory_content_map = dirctory_content_map(fsimage_tree)

    #call dfs for 1 node : testing pupose
    path_dfs = dfs(ad_list_test, '16385', '16391', path = [], visited = set())
    print('path_dfs>',path_dfs)
    


def dirctory_content_map(fsimage_tree):  
    directory_content_map = defaultdict(list)
    inode_count1 = fsimage_tree.xpath('/fsimage/INodeSection/numInodes/text()')[0]
    inode_count = int(inode_count1)
    root_directory = ''
    if(fsimage_tree.xpath('/fsimage/INodeSection/inode[name[not(node())]]')):
        root_directory = fsimage_tree.xpath('/fsimage/INodeSection/inode[name[not(node())]]/id/text()')[0]
    id_list = fsimage_tree.xpath('/fsimage/INodeSection/inode/id/text()')
    type_list = fsimage_tree.xpath('/fsimage/INodeSection/inode/type/text()')
    name_list = fsimage_tree.xpath('/fsimage/INodeSection/inode/name/text()')
    mtime_list = fsimage_tree.xpath('/fsimage/INodeSection/inode/mtime/text()')
    permission_list = fsimage_tree.xpath('/fsimage/INodeSection/inode/permission/text()')
    info_list = [id_list, type_list, mtime_list, permission_list]
    
    k = 0
    for elem in id_list:
        print('elem>',elem)
        if int(elem) == int(root_directory):
            directory_content_map[elem].append('ROOTROOT')
        else:
            directory_content_map[elem].append(name_list[k])
            k+=1

    for i in range(inode_count):
        for element in info_list:
            directory_content_map[id_list[i]].append(element[i])
        
    print('directory_content_map>>',directory_content_map)
    return directory_content_map


def create_inode_directory_structure(inode_directory):
    inode_directory_list = []
    if(len(inode_directory) != 0):
        for element in inode_directory:
            parent = ''
            child = []
            tempDict = {}
            for directory in element:
                if(directory.tag == 'parent' and directory.text):
                    parent = directory.text
                    print('type parent',type(parent))
                elif(directory.tag == 'child' and directory.text):
                    child.append(directory.text )
            tempDict[parent] = child
            inode_directory_list.append(tempDict)
    
    print('inode_directory_list> ',inode_directory_list)
    return inode_directory_list

def dfs(inode_directory_list, start, target, path = [], visited = set()):
    print('-----dfs-----')
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for (neighbour) in inode_directory_list[start]:
        print('neighbour>>',neighbour)
        if neighbour not in visited:
            result = dfs(inode_directory_list, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None 

        



if __name__ == "__main__":
    main()