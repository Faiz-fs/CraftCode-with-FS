
/*let x=10;
const u=20;

//Variable
console.log(a);
a=2;
console.log(a);


//LET
console.log(x);
x=200;
console.log(x);

//constant
console.log(u);
u=11;
console.log(u);*/ 


 // Hoisting
var a=10;
function codehoist(){
    var b=20;
    a=100; //100

}
codehoist();
console.log(a);
//console.log(b);
