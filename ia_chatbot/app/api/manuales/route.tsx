import axios from 'axios';
import * as dotenv from 'dotenv';
import qs from 'qs';
import { Manual } from '@/styles/types';
dotenv.config();
//llamada a api interna para poder llamar a dotenv y no desvelar las claves 
export  async function GET() { 
    const client_id = process.env.client_id!;
    const client_secret = process.env.client_secret!;
    const tenant_id = process.env.tenant_id!;
    const tenant = process.env.tenant!;
    const url1 = process.env.url1!;
    const url= process.env.url!;

    const data = qs.stringify({
      grant_type: 'client_credentials',
      resource: `00000003-0000-0ff1-ce00-000000000000/${tenant}.sharepoint.com@${tenant_id}`,
      client_id,
      client_secret,
    });
    
    const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
      };
    
      try {
        const response = await axios.post(url1, data, { headers });//llamada Oauth
        const json_auth:string= response.data.access_token
        const headers2 = {
            'Authorization': "Bearer " + json_auth,
            'Accept':'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose'
        }
        const datosmanuales= await axios.get(url, { headers: headers2 })//llamda api para tomar manuales
        const printdata:Manual[]=[]
        for(let i=0; i<datosmanuales.data.d.results.length; i++){
            printdata.push({
                url: datosmanuales.data.d.results[i].PDF_Manual.Url,
                descripcion:datosmanuales.data.d.results[i].Descripci_x00f3_n})
        }
        return new Response(JSON.stringify(printdata), {
            status: 200,
        })
      } catch (error) {
        if (axios.isAxiosError(error)) {
          console.error("Error en la llamada API:", error.response?.data || error.message);
        } else {
          console.error("Error inesperado:", error);
        }
        return new Response("Error en la llamada API", {
          status: 500,
        });
      }
}