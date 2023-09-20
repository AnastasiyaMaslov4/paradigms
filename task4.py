from scipy.stats import pearsonr

arr1 = [2, 4, 6, 8]
arr2= [0, 17, 7, 9]

def corellation(arr1, arr2):
    corr, _ = pearsonr(arr1, arr2)
    print('Pearsons correlation: %.3f' % corr)

corellation(arr1,arr2)