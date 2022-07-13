// recipe finder


function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    getInputValue(data)
}



function getInputValue() {
    var searchRecipe = document.getElementById('search').value;

    sendApiRequest(searchRecipe)
}


async function sendApiRequest(searchRecipe) {
    let APP_ID = "8be89793"
    let APP_KEY = "2875be21556b0639a442be2516bf5f9e"
    let find = searchRecipe

    try {
        let response = await fetch(`https://api.edamam.com/api/recipes/v2?type=public&q=${find}&app_id=${APP_ID}&app_key=${APP_KEY}`)
        let data = await response.json()
        useApiData(data)
    }
    catch (error) {
        console.log(error);
    }
}


function useApiData(data) {
    let recipes = " "
    for (var item of data.hits) {
        recipes += `<div class="card m-5 rounded shadow-lg" style="width: 18rem;">
                    <img src="${item.recipe.image}" class="card-img-top" alt="recipe">
                    <div class="card-body">
                        <h5 class="card-title mt-2">${item.recipe.label}</h5>
                        <a href=${item.recipe.url} class="btn btn-primary mt-3">Recipe</a>
                        </div>
                        </div>
                        `
        document.getElementById('recipes').innerHTML = recipes
    }
}



