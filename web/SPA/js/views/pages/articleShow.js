import ArticleProvider from "../../services/articleProvider.js";

export default class ArticleShow{
    async render(Index=null) {
    let article = await ArticleProvider.getArticle(Index);
    console.log(article);
    let view = `
        <section>
            <h2>${article.title}</h2>
            <p> Index : ${article.id}</p>
            <p>${article.text}</p>
        </section>
        `;

        return view
    }
}