var scriptTags = document.getElementsByTagName('script');

(function(){

    if(navigator.onLine){
    } else {
        console.log(scriptTags);
        console.log(scriptTags.length);
        // rewrite script tags.
        for(var j = 0; j < scriptTags.length; j++){
            var s = scriptTags.item(j);
            console.log(s);
            if(s.hasAttribute('src')){
                console.log("attribute: " + s.getAttribute('src'));
            }
        }

    }
    
})();