var statements = [
    "I like coins.",
    "coins are made of metal.",
    "99% of numismatist quit before their big find.",
    "mhhhh mhhhh yummm coins.",
    "whats better than one coin? a lot of em.",
    "there are 150 million coin collectors in the us.",
    "You miss 100% of the coins you don't find.",
    "you can consume coins.",
    "there are people in your walls.",
    "Hello Kitty collects coins."
];

// Function to get a random statement
function getRandomStatement() {
    var randomIndex = Math.floor(Math.random() * statements.length);
    return statements[randomIndex];
}

// Display the random statement on the page
window.onload = function() {
    var statementElement = document.getElementById('random-statement');
    statementElement.textContent = getRandomStatement();
};