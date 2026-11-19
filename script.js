const saveName = document.getElementById("nameInput");
const saveButton = document.getElementById("saveButton");
const clearName = document.getElementById("clearButton");
const greeting =document.getElementById("greeting");

//accessing local storage
//try to find item called username
//if its there, get the item and store that into savedname

let savedName = localStorage.getItem("username");

if(savedName !== null) {
    greeting.textContent = "Welcome back, " + savedName;
}

function savingName() {
    let name = nameInput.value;
    localStorage.setItem("username", name);
    greeting.textContent = "Welcome, " + name;
}
saveButton.addEventListener("click", savingName);

function clearingName() {
    localStorage.removeItem("username");
    greeting.textContent = "";
    nameInput.value = "";
}

clearButton.addEventListener("click", clearingName);