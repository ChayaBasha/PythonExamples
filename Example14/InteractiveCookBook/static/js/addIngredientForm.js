

function addIngredientFields() {
    document.getElementById("ingredient-fieldset").insertAdjacentHTML('beforeend',
        '<br>' +
        '<label for="ingredient_name">Ingredient</label>\n' +
        '        <input type="text" name="ingredient_name" id="ingredient_name" placeholder="Ingredient Name">\n' +
        '        <label for="amount">Amount</label>\n' +
        '        <input type="number" name="amount" id="amount" placeholder="3">\n' +
        '        <label for="unit>">units</label>\n' +
        '        <input type="text" name="unit" id="unit" placeholder="Tbs">\n' +
        '        <input type="button" value=" + " onclick="addIngredientFields()" >' +
        '         <br>' );
}