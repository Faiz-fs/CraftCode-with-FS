
const mysql=require('mysql');

const con=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Mohfaiz@543",
    database:"mysqljs",
});

con.connect((error)=>{
    if(error){
        console.log("Not connected");
        return;
    }
    console.log("connected");

    con.query("select * from jstut;",(err,data,field)=>{
        if(err){
            console.log(err);
        }
        else{
            console.log("connected")
        }
    });
});