import { method } from "lodash";
import { ENDPOINT } from "../config.js";
import { json } from "body-parser";

export default class ArticleProvider{
    static fetchArticle = async(limit = 1) => {
        const options = {
            method: 'GET',
            headers:{
                "Content-Type": "application/json",
            }
        }
        try{
            const response = await fetch( `${ENDPOINT}?_page=0${limit}`, options)
            const JSON = await response.json();
            return json.data
        }catch(err){
            console.error(err)
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
            const JSON = await response.json();
            return json
        }catch(err){
            console.log("Error getting doc", err)
        }
    }
}