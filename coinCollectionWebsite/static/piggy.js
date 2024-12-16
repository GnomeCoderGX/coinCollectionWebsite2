var denominations = [
    "dime",
    "quarter",
    "nickel",
    "penny",
    "halfDollar",
    "doubloon"
];

var conditions =[
   "mint",
   "poor",
   "mid",
   "good"
];

function fx(){
    alert("coin!")
    var denomination = denominations[Math.floor(Math.random() * denominations.length)]
    var condition = conditions[Math.floor(Math.random() * conditions.length)]
    var year = Math.floor(Math.random() * (2020 - 1820 + 1) + 1820)
    console.log(year)
    var xhttp = new XMLHttpRequest()

    xhttp.onreadystatechange = function(){
        if(this.readystate === 4 && this.status === 200){
            console.log(this.responseText)
            console.log(this.status)

        }

    }

    data = {den: denomination, condish: condition, yr : year}
    xhttp.open("POST", "/piggybank")
    console.log(data)
    xhttp.send(data)
}