// alert("This is what Manvitha wants")

alert("Hi you guys welcome to my website!!Do you want to learn about dogs and cats to see who you are?");
let cats="cats";
let dogs="dogs";
const avgAgeOfDogs=12;
const avgAgeOfCats=16;
let avgAmountOfTimesPeopleUsedThisWebsite=2;
console.log('how long the dogs live for!' , avgAgeOfDogs);
console.log('how long the cats live for!' , avgAgeOfCats);
let dogEntries=1;
let catEntries=1;

console.log('Total number of linked sites: ', dogEntries + catEntries);

let adoptedDogsAndCats=0

if (adoptedDogsAndCats > 0 || adoptedDogsAndCats < 20) {
    console.log('Good job, but always remember that slow and steady wins the race.')
} else {
    console.log('Awesome job!')
}
console.log(DogsAndCats);

document.getElementById("dogsBtn").addEventListener("click", function() {
    window.location.href = "dogs.html";  // Replace with your desired URL
});
