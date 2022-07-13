// console.log('test')



// drop down list for recipe create

var selectElem = document.getElementById('pantry')

var obj = {
    'none':[],
    'dry_goods':['produce', 'starch', 'spices', 'miscellaneous'],
    'fridge':['protein','produce', 'starch', 'dairy', 'condiments'],
    'freezer':['protein','produce', 'starch', 'miscellaneous'],
    'utilities':['utilities'],

}

selectElem.addEventListener('change', function () {
    var change = selectElem.value;
    console.log(selectElem.value)
    let data = " "
    for(var item of obj[change]){
        // console.log(item);
        data += `<option value="${item}">${item[0].toUpperCase() + item.slice(1)}</option>`
    }
    // console.log(data);
    document.getElementById('pantry_group').innerHTML = data


})


