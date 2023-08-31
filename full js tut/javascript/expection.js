/*try and catch
var a=10;
var b=0;
try {
    console.log(a/b);
} catch (error) {
    console.log(error);
}
*/

/*throw

var a=12;

if(a<10){
    throw "value is low";
}
else{
    throw "value is high";
}
*/

//finally

var a=10;
var b=0;
try {
    console.log(a/b);
} catch (error) {
    console.log(error);
}
finally{
    b=10;
    console.log("finally statement check",a/b);
}