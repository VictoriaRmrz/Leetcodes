from collections import defaultdict
class Solution(object):
    # Cuenta cuantos arrays hay que formenk    
    def count_subarray(self,nums, k):
        hash_map = defaultdict(int) # guardar el numero de incidencias (cuantas veces aparece esta suma)
        hash_map[0] = 1 # inicializar que la suma de 0 ocurre 1 vez
        current_sum = 0
        length = 0

        for num in nums:
            # si nums[i:j] = k
            # nums[j] - nums[i] = k = length
            # current_sum - k = length
            current_sum += num
            length += hash_map.get(current_sum - k, 0) # .get() sirve para evitar que arroje un
                                                       # error si no encuentra el numero en la hash
            hash_map[current_sum] += 1

        return length
    
    def max_length_subarray(self, nums, k):
        hash_map = {}
        current_sum = 0
        max_length = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum == k: # Si la suma actual es igual a k
                max_length = i + 1 # Actualiza la longitud máxima
            if current_sum - k in hash_map: # Si el numero ya esta repetido, encontro un nuevo subarray
                length = i - hash_map[current_sum - k] # calcula la longitud como: donde encontro la suma k hasta la nueva coincidencia de suma k
                max_length = max(max_length, length) # obtiene cual de las veces que encontre suma k, es la mayor

            hash_map[current_sum] = i # se guarda el indice de lo que va sumando cada cosa

        return max_length

def main():
    nums = [3, -2, 5, -1, 2, -3, 4]
    k = 4
    sol = Solution()
    result = sol.max_subarray_len(nums, k)
    print(result)

if __name__ == "__main__":
    main()