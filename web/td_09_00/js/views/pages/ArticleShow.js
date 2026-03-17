import Utils        from '../../services/Utils.js'
import ArticleProvider from "./../../services/ArticleProvider.js";

export default class ArticleShow {
    async render () {
        let request = Utils.parseRequestURL()
        let post = await ArticleProvider.getArticle(request.id)

        return /*html*/`
            <section class="section">
                <h1>${post.title}</h1>
                <p>Reactions +
                    <span id="counter">${post.reactions}</span> 
                    <a href="#" id="add-r" data-count="${post.reactions}"><i class="bi bi-hand-thumbs-up" style="font-size: 1.3rem;"></i></a></p>
                <p> Post Content : ${post.body} </p>
                <p> Post tags : ${post.tags.join(', ')} </p>
                <p>Comments<p>
                    <ul>
                    ${ post.comments.map(comment => 
                        /*html*/`
                        <li class="row">
                            <p class="col-2">${comment.user.username}</p>
                            <p class="col-10">${comment.body}</p>
                        </li>
                        `
                        ).join('\n ')
                    }
                    </ul>
            </section>
            <p><a href="/">back to home</a></p>
            <p><a href="#/articles">back to all articles</a></p>
        `
    }
    
    async after_render () {
        document.querySelector('#add-r').addEventListener ('click',  async (e) => {
            e.preventDefault();
            let count = +e.target.parentNode.dataset.count;
            e.target.parentNode.dataset.count++;
            count++;
            let request = Utils.parseRequestURL();
            let response = await ArticleProvider.addReaction(request.id, count);
            let counter = document.querySelector('#counter');
            counter.textContent = count;
            const toastBt = bootstrap.Toast.getOrCreateInstance('#success-toast');
            toastBt.show();
        });
    }
}

