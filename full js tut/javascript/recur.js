//factorial

function fact(n){
    if(n==0){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}

var result= fact(5);

console.log("the factorial of 5 is ",result);