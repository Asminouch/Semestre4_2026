
import { ENDPOINT } from "../config.js";


export default class ArticleProvider{
    static fetchArticle = async(limit = 10) => {
        const options = {
            method: 'GET',
            headers:{
                "Content-Type": "application/json",
            }
        }
        try{
            const response = await fetch( `${ENDPOINT}?_page=1&_per_page=${limit}`, options)
            const json = await response.json();
            return json.data
        }catch(err){
            console.error("Error getting doc", err)
        }
    }

    static getArticle = async (id)=>{
        const options = {
            method: 'GET',
            headers:{
                "Content-Type": "application/json",
            }
        }
        try{
            const response = await fetch( `${ENDPOINT}/`+id, options)
            const json = await response.json();
            return json
        }catch(err){
            console.log("Error getting doc", err)
        }
    }
}