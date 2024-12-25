import express from 'express';
import swaggerUi from 'swagger-ui-express';
import swaggerSpec from './config/swagger.js';


import { Sequelize } from 'sequelize';
import userModel from './models/user.js';
import userRoutes from './router/userRoutes.js';


const app = express();
const port = 3000;


app.use('/api', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use(express.json());

const sequelize = new Sequelize('postgres', 'postgres', 'postgres', {
    host: 'localhost',
    dialect: 'postgres',
});

const User = userModel(sequelize);

sequelize.sync()
    .then(() => console.log('Model zsynchronizowany z bazą danych!'))
    .catch(err => console.error('Błąd synchronizacji:', err));

app.use('/users', userRoutes(User));

app.listen(port, () => console.log(`Listening on port ${port}`));
