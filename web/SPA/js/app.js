import Utils  from "./services/utils.js";
import ArticleAll from "./views/pages/articleAll.js";
import ArticleShow from "./views/pages/articleShow.js";
import About from "./views/pages/About.js";
import Home from "./views/pages/home.js";
import Error404 from "./views/pages/error404.js";

const routes = {
    "/": Home,
    "/about": About,
    "/articles": ArticleAll,
    "/articles/:id": ArticleShow

};

const router = async()=>{
    const content = null ||  document.querySelector('#main');

    let request = Utils.parseRequestUrl();

    let parsedURL= (request.ressource ? '/'+ request.ressource : '/') + (request.id ? '/:id': '')+ (request.verb ? '/'+ request.verb: '');

    let pageC = routes[parsedURL] ? routes[parsedURL] :  Error404;

    let page= new pageC();

    content.innerHTML = await page.render(request.id);
}

window.addEventListener("hashchange", router);

window.addEventListener("load",router);