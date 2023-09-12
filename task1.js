// Задача №1
// Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для 
// сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

function sortNums (array) {
    for (let j = 0; j < array.length - 1; j++) {
        for (let i = 0; i < array.length - 1 - j; i++) {
            let swipe = 0;
            if(array[i] < array[i+1]) {
                swipe = array[i];
                array[i] = array[i+1];
                array[i+1] = swipe;
            }  
        }
    }
}

let arr = [2, 4, 10, 1, 0];
sortNums(arr);
console.log(arr);

// Задача №2
// Написать точно такую же процедуру, но в декларативном стиле

function sortNums2(array) {
    array.sort((a,b) => b-a);
}

let arr2 = [-1, 10, 16, 5, 4];
sortNums2(arr2);
console.log(arr2);