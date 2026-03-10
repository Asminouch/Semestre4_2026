import ArticleProvider from "../../services/articleProvider.js";

export default class ArticleAll{
    static async render(){
    let articles = await ArticleProvider.fetchArticle(10);
    let view = `
        <h2>Tous les articles</h2>
        <ul>
            ${articles.map(
                article =>
                    `<ul>
                        <li>${article.title}</li>
                    </ul>`
            ).join('\n')}
        </ul>
    `;
    return view;
    }
}