import request from 'supertest';
import express from 'express';
import userRoutes from '../router/userRoutes';
import userModel from '../models/user';
import { Sequelize } from "sequelize";

const app = express();
app.use(express.json());

const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: ':memory:',
    logging: false,
});

const User = userModel(sequelize);

app.use('/users', userRoutes(User));

beforeAll(async () => {
    await sequelize.authenticate();
    await sequelize.sync({ force: true });
});

afterAll(async () => {
    await sequelize.close();
});

describe('Test api użytkowników', () => {

    it('GET /users - Sprawdzenie, czy odpowiedź zawiera listę użytkowników', async () => {
        const response = await request(app)
            .get('/users')
            .expect(200);

        expect(Array.isArray(response.body)).toBe(true);
    });

    it('GET /users/:id - Sprawdzenie, czy odpowiedź dla istniejącego użytkownika zwraca poprawne dane', async () => {
        const newUser = {
            firstName: 'Jan',
            lastName: 'Kowalski',
            email: 'jan.kowalski@example.com',
        };

        const createResponse = await request(app)
            .post('/users')
            .send(newUser)
            .expect(201);

        const userId = createResponse.body.id;

        const response = await request(app)
            .get(`/users/${userId}`)
            .expect(200);

        expect(response.body.firstName).toBe(newUser.firstName);
        expect(response.body.lastName).toBe(newUser.lastName);
        expect(response.body.email).toBe(newUser.email);
    });

    it('GET /users/:id - Sprawdzenie, czy odpowiedź dla nieistniejącego użytkownika zwraca odpowiedni błąd (404)', async () => {
        const response = await request(app)
            .get('/users/999999')
            .expect(404);

        expect(response.body.error).toBe('Użytkownik nie znaleziony');
    });

    it('POST /users - Sprawdzenie, czy możliwe jest dodanie nowego użytkownika', async () => {
        const newUser = {
            firstName: 'Krystian',
            lastName: 'Jank',
            email: 'krystian.jank@example.com',
        };

        const response = await request(app)
            .post('/users')
            .send(newUser)
            .expect(201);

        expect(response.body.firstName).toBe(newUser.firstName);
        expect(response.body.lastName).toBe(newUser.lastName);
        expect(response.body.email).toBe(newUser.email);
    });

    it('POST /users - Testowanie przypadku, gdy dane wejściowe są niekompletne (brak wymaganych pól)', async () => {
        const newUser = {
            firstName: 'Krystian',
            lastName: 'Jank',
        };

        const response = await request(app)
            .post('/users')
            .send(newUser)
            .expect(400);

        expect(response.body.error).toBe('Błąd walidacji: notNull Violation: User.email cannot be null');
    });

    it('PUT /users/:id - Sprawdzenie, czy możliwa jest aktualizacja danych użytkownika', async () => {
        const newUser = {
            firstName: 'test',
            lastName: 'test',
            email: 'test.jank@example.com',
            admin:false
        };

        const createResponse = await request(app)
            .post('/users')
            .send(newUser)
            .expect(201);

        const userId = createResponse.body.id;

        const updatedUser = {
            firstName: 'Krystian',
            lastName: 'Jankowski',
            email: 'krystian.jankowski@example.com',
        };

        const response = await request(app)
            .put(`/users/${userId}`)
            .send(updatedUser)
            .expect(200);

        expect(response.body.firstName).toBe(updatedUser.firstName);
        expect(response.body.lastName).toBe(updatedUser.lastName);
        expect(response.body.email).toBe(updatedUser.email);
    });

    it('PUT /users/:id - Sprawdzenie, czy próba zaktualizowania nieistniejącego użytkownika zwróci błąd', async () => {
        const updatedUser = {
            firstName: 'Krystian',
            lastName: 'Jankowski',
            email: 'krystian.jankowski@example.com',
        };

        //zakładam ze nie mamy tylu uzytkownikow w aplikacji
        const response = await request(app)
            .put('/users/999999')
            .send(updatedUser)
            .expect(404);

        expect(response.body.error).toBe('Użytkownik nie znaleziony');
    });

    it('DELETE /users/:id - Sprawdzenie, czy użytkownik może zostać usunięty', async () => {
        const newUser = {
            firstName: 'Krystian',
            lastName: 'Jank',
            email: 'krystian@example.com',
            admin:false
        };

        const createResponse = await request(app)
            .post('/users')
            .send(newUser)
            .expect(201);

        const userId = createResponse.body.id;

        const deleteResponse = await request(app)
            .delete(`/users/${userId}`)
            .expect(200);

        expect(deleteResponse.body.message).toBe('Użytkownik usunięty');
    });

    it('DELETE /users/:id - Sprawdzenie, czy po usunięciu użytkownika próba jego odczytu zwróci błąd (404)', async () => {
        const newUser = {
            firstName: 'Krystian',
            lastName: 'Jank',
            email: 'jank@example.com',
            admin:false
        };

        const createResponse = await request(app)
            .post('/users')
            .send(newUser)
            .expect(201);

        const userId = createResponse.body.id;

        await request(app)
            .delete(`/users/${userId}`)
            .expect(200);

        const response = await request(app)
            .get(`/users/${userId}`)
            .expect(404);

        expect(response.body.error).toBe('Użytkownik nie znaleziony');
    });
});
