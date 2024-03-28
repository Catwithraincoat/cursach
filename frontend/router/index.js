import {createRouter, createWebHistory} from 'vue-router';
import routes from './routes.js';
import 'remixicon/fonts/remixicon.css';


const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;