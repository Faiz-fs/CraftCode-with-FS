var getname = document.getElementById("name");
var username = document.getElementById("username");
var gender = document.getElementsByName("gender");
var passwd = document.getElementById("passwd");
var submit = document.getElementById("submit");
var formid = document.getElementById("formid");
var tableb = document.getElementById("tablebody");
var data = "";
let newarray = [];

function enform() {
  document.getElementById("namecon").innerText = "";
  document.getElementById("usercon").innerText = "";
  document.getElementById("passcon").innerText = "";
  document.getElementById("gendcon").innerText = "";
  let found = 0;
  for (i = 0; i < newarray.length; i++) {
    if (newarray[i].username == username.value) {
      found = 1;
    }
  }
  if (found == 1) {
    alert("user already exsist");
  } else {
    if (
      getname.value != "" &&
      username.value != "" &&
      passwd.value.length >= 6 &&
      radiodisplay() != ""
    ) {
      adddata();
      document.getElementById("namecon").innerText = "";
      document.getElementById("usercon").innerText = "";
      document.getElementById("passcon").innerText = "";
      document.getElementById("gendcon").innerText = "";
      formid.reset();
    } else {
      if (getname.value == "") {
        document.getElementById("namecon").style.color = "red";
        document.getElementById("namecon").innerText = "Name is empty";
      }
      if (username.value == "") {
        document.getElementById("usercon").style.color = "red";
        document.getElementById("usercon").innerText = "username is empty";
      }
      if (passwd.value.length < 6) {
        console.log("pass");
        document.getElementById("passcon").style.color = "red";
        document.getElementById("passcon").innerText =
          "password should have 6 char";
      }
      if (radiodisplay() == "") {
        console.log("gend");
        document.getElementById("gendcon").style.color = "red";
        document.getElementById("gendcon").innerText = "select any one gender";
      }
    }
  }
}
function adddata() {
  var tabledata = ``;
  let value = {
    name: getname.value,
    username: username.value,
    password: passwd.value,
    gender: radiodisplay(),
  };
  //console.log(value);
  newarray.push(value);
  console.log(newarray);
  formid.reset();
  newarray.forEach((value) => {
    tabledata += `<tr id="${value.username}">
        <td>${value.name}</td>
        <td>${value.username}</td>
        <td>${value.password}</td>
        <td>${value.gender}</td>
        <td><button onclick="editform(this)">Update</button> | <button onclick="deleterow(this)">Delete</button></td>
        </tr>`;
  });
  tableb.innerHTML = tabledata;
}

function radiodisplay() {
  for (i = 0; i < gender.length; i++) {
    if (gender[i].checked) {
      return gender[i].value;
    }
  }
  return "";
}

function editform(obj) {
  var td = event.target.parentNode.parentNode;
  data = td.getAttribute("id");
  //console.log(data);
  for (i = 0; i < newarray.length; i++) {
    if (newarray[i].username == data) {
      getname.value = newarray[i].name;
      username.value = newarray[i].username;
      passwd.value = newarray[i].password;
      if (newarray[i].gender == "Male") {
        document.getElementById("male").checked = "true";
      } else if (newarray[i].gender == "Female") {
        document.getElementById("female").checked = "true";
      }
    }
  }
  document.getElementById("updt").removeAttribute("hidden");
  document.getElementById("submit").hidden = true;
}

function updateform() {
  var tabledata = ``;
  //console.log(getname.value,username.value,data)
  for (i = 0; i < newarray.length; i++) {
    if (newarray[i].username == data) {
      newarray[i].name = getname.value;
      newarray[i].username = username.value;
      newarray[i].password = passwd.value;
      newarray[i].gender = radiodisplay();
    }
  }
  console.log(newarray);
  newarray.forEach((value) => {
    tabledata += `<tr id="${value.username}">
        <td>${value.name}</td>
        <td>${value.username}</td>
        <td>${value.password}</td>
        <td>${value.gender}</td>
        <td><button onclick="editform(this)">Update</button> | <button onclick="deleterow(this)" >Delete</button></td>
        </tr>`;
  });
  tableb.innerHTML = tabledata;
  formid.reset();
  document.getElementById("submit").hidden = false;
  document.getElementById("updt").hidden = true;
}

function deleterow(obj) {
  //console.log("hello");
  var tabledata = ``;
  var td = event.target.parentNode.parentNode;
  data = td.getAttribute("id");
  for (i = 0; i < newarray.length; i++) {
    if (newarray[i].username == data) {
      newarray.splice(i, 1);
    }
  }
  newarray.forEach((value) => {
    tabledata += `<tr id="${value.username}">
        <td>${value.name}</td>
        <td>${value.username}</td>
        <td>${value.password}</td>
        <td>${value.gender}</td>
        <td><button onclick="editform(this)">Update</button> | <button onclick="deleterow(this)" >Delete</button></td>
        </tr>`;
  });
  tableb.innerHTML = tabledata;
  //formid.reset();
}
