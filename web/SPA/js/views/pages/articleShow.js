import ArticleProvider from "../../services/articleProvider.js";

export default class ArticleShow{
    static async render() {
    let article = ArticleProvider.getArticle('f25b');
    let view = `
        <section>
            <h2>${article.title}</h2>
            <p> Index : ${article.index}</p>
            <p>${article.text}</p>
        </section>
        `;

        return view
    }
}