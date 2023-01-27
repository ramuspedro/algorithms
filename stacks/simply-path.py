# https://leetcode.com/problems/simplify-path/

# dicionario com operações
# / -> separação de um diretório
# // ou mais -> separação de diretório
# .. -> remover o diretório anterior

# se eu fizer um split, eu vou me resumir -> 
# .  -> permanece
# .. -> remove

class Solution:
    def simplifyPath(self, path: str):
        path_splited = path.split("/")
        result = []

        for el in path_splited:
            if el == "..":
                if len(result) > 0:
                    result.pop()
            elif el == "." or el == "":
                pass
            else:
                result.append(el)
        
        return "/" + "/".join(result)


solution = Solution()

exs = [
    "/home/", 
    "/../", 
    "/home//foo/", 
    "/home/../casa/", 
    "/../casa///cozinha", 
    "/../casa/banheiro/.../quarto/", 
    "/../casa/banheiro/..././quarto/",
    "/../casa////cozinha"]

for el in exs:
    print("result = ", solution.simplifyPath(el))