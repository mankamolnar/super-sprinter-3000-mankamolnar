$(document).ready(function() {
    $("#business_value").TouchSpin({
        min: 100,
        max: 1500,
        step: 100,
        initval: 100,
        decimals: 0,
        verticalbuttons: true
    });

    $("#estimation").TouchSpin({
        min: 0.5,
        max: 1500,
        step: 0.5,
        initval: 0.5,
        decimals: 1,
        verticalbuttons: true
    });
});