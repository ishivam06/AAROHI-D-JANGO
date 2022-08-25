
$(function(){

    function setHeight(){
        $(".response").each(function(index,element){
            var target = $(element);
            target.removeClass("fixed-height");
            var height = target.innerHeight();
            target.attr("data-height", height)
                .addClass("fixed-height");
        });
    };

    $("input[name=question]").on("change", function(){
        $("p.response").removeAttr("style");

        var target = $(this).next().next();
        target.height(target.attr("data-height"));
    })

    setHeight();
});

// function slideFaq()
// {
//     document.getElementById('faqs-ans-1').style.display="block";
//     document.getElementById('faq-ans-1').style.height = "600px";
// }

