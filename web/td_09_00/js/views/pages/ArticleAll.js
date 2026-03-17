import ArticleProvider from "../../services/ArticleProvider.js";

export default class ArticleAll {

    async render () {
        let articles = await ArticleProvider.fetchArticles(50);
        let view =  /*html*/`
            <h2>Tous articles</h2>
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                ${ articles.map(article => 
                    /*html*/`
                    <div class="col">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <img class="bd-placeholder-img card-img-top" data-src="https://placehold.co/600x400?text=${encodeURI(article.title)}" />
                            <p class="card-text">${article.text ? article.text.slice(0,100) : ''}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                <a href="#/articles/${article.id}" class="btn btn-sm btn-outline-secondary">Voir ${article.title}</a>
                                </div>
                                <small class="text-body-secondary">
                                    ${article.reactions} <i class="bi bi-hand-thumbs-up" style="font-size: 1.3rem;"></i>
                                </small>
                            </div>
                        </div>
                    </div>
                    </div>
                    `
                    ).join('\n ')
                }
            </div>
        `
        return view
    }

    async after_render () {

        // Go image lazy loading
        let options = {
            root: null,
            rootMargin: "0px",
            threshold: 0.2,
        };

        let observer = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (entry.target.src === '' && entry.intersectionRatio === 1) {
                    entry.target.src = entry.target.dataset.src;
                }
            })
        }, options);

        let collections = document.querySelectorAll('img.card-img-top');
        collections.forEach((entry) => {
            observer.observe(entry);
        })

    }

}