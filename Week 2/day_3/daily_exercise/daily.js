let arr = [5,0,9,1,7,4,2,6,3,8];

function bubble_Sort(arr) {
    let swap;
    let n = arr.length-1;
    let x=arr;
    do {
        swap = false;
        for (let i=0; i < n; i++) {

            if (x[i] < x[i+1]) {
            
               let temp = x[i];
               x[i] = x[i+1];
               x[i+1] = temp;
               swap = true;
            }
        }
        n--;
    } while (swap);
 return x; 
}

console.log(bubble_Sort(arr));

arr = arr.toString()

console.log(arr)