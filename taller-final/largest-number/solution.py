class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mitad = len(arr) // 2
            izquierda = mergeSort(arr[:mitad])
            derecha = mergeSort(arr[mitad:])

            resultado = []
            i = 0
            j = 0

            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] + derecha[j] >= derecha[j] + izquierda[i]:
                    resultado.append(izquierda[i])
                    i += 1
                else:
                    resultado.append(derecha[j])
                    j += 1

            resultado.extend(izquierda[i:])
            resultado.extend(derecha[j:])

            return resultado

        nums = mergeSort(nums)
        resultado = "".join(nums)

        if resultado[0] == "0":
            return "0"

        return resultado