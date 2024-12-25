import express from 'express';

const router = express.Router();

export default (User) => {

    /**
     * @swagger
     * /users:
     *   post:
     *     summary: Tworzy nowego użytkownika.
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               firstName:
     *                 type: string
     *               lastName:
     *                 type: string
     *               email:
     *                 type: string
     *               admin:
     *                 type: boolean
     *     responses:
     *       201:
     *         description: Użytkownik dodany.
     *       400:
     *         description: Błąd walidacji.
     */
    router.post('/', async (req, res) => {
        try {
            const user = await User.create(req.body);
            res.status(201).json(user);
        } catch (err) {
            res.status(400).json({ error: 'Błąd walidacji: ' + err.message });
        }
    });

    /**
     * @swagger
     * /users/{id}:
     *   patch:
     *     summary: Akutalizuje użytkownika.
     *     parameters:
     *       - in: path
     *         name: id
     *         required: true
     *         description: ID użytkownika do aktualizacji
     *         schema:
     *           type: integer
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               firstName:
     *                 type: string
     *               lastName:
     *                 type: string
     *               email:
     *                 type: string
     *               admin:
     *                 type: boolean
     *     responses:
     *       200:
     *         description: Użytkownik zaktualizowany.
     *       404:
     *         description: Użytkownik nie znaleziony.
     *       400:
     *         description: Błąd walidacji.
     */
    router.patch('/:id', async (req, res) => {
        try {
            const user = await User.findByPk(req.params.id);

            if (!user) {
                return res.status(404).json({ error: 'Użytkownik nie znaleziony' });
            }

            await user.update(req.body);
            res.status(200).json(user);
        } catch (err) {
            res.status(400).json({ error: 'Błąd walidacji: ' + err.message });
        }
    });

    /**
     * @swagger
     * /users/{id}:
     *   put:
     *     summary: Akutalizuje użytkownika.
     *     parameters:
     *       - in: path
     *         name: id
     *         required: true
     *         description: ID użytkownika do aktualizacji
     *         schema:
     *           type: integer
     *     requestBody:
     *       required: true
     *       content:
     *         application/json:
     *           schema:
     *             type: object
     *             properties:
     *               firstName:
     *                 type: string
     *               lastName:
     *                 type: string
     *               email:
     *                 type: string
     *               admin:
     *                 type: boolean
     *     responses:
     *       200:
     *         description: Użytkownik zaktualizowany.
     *       404:
     *         description: Użytkownik nie znaleziony.
     *       400:
     *         description: Błąd walidacji.
     */
    router.put('/:id', async (req, res) => {
        try {
            const user = await User.findByPk(req.params.id);

            if (!user) {
                return res.status(404).json({ error: 'Użytkownik nie znaleziony' });
            }

            await user.update(req.body);
            res.status(200).json(user);
        } catch (err) {
            res.status(400).json({ error: 'Błąd walidacji: ' + err.message });
        }
    });

    /**
     * @swagger
     * /users:
     *   get:
     *     summary: Pobiera listę użytkowników.
     *     responses:
     *       200:
     *         description: Lista użytkowników.
     *       500:
     *         description: Błąd serwera.
     */
    router.get('/', async (req, res) => {
        try {
            const users = await User.findAll();
            res.status(200).json(users);
        } catch (err) {
            res.status(500).json({ error: 'Błąd serwera: ' + err.message });
        }
    });

    /**
     * @swagger
     * /users/{id}:
     *   delete:
     *     summary: Usuwa użytkownika.
     *     parameters:
     *       - in: path
     *         name: id
     *         required: true
     *         description: ID użytkownika do usunięcia
     *         schema:
     *           type: integer
     *     responses:
     *       200:
     *         description: Użytkownik usunięty.
     *       404:
     *         description: Użytkownik nie znaleziony.
     *       500:
     *         description: Błąd serwera.
     */
    router.delete('/:id', async (req, res) => {
        try {
            const user = await User.findByPk(req.params.id);

            if (!user) {
                return res.status(404).json({ error: 'Użytkownik nie znaleziony' });
            }

            // dodane sprawdzanie, czy użytkownik jest administratorem,potrzebne do testu z deletem
            if (user.admin === true) {
                return res.status(403).json({ error: 'Nie masz uprawnień do usunięcia administratora' });
            }

            await user.destroy();
            res.status(200).json({ message: 'Użytkownik usunięty' });
        } catch (err) {
            res.status(500).json({ error: 'Błąd serwera: ' + err.message });
        }
    });

    /**
     * @swagger
     * /users/{id}:
     *   get:
     *     summary: Pobranie użytkownika.
     *     parameters:
     *       - in: path
     *         name: id
     *         required: true
     *         description: ID użytkownika
     *         schema:
     *           type: integer
     *     responses:
     *       200:
     *         description: Użytkownik znaleziony.
     *         content:
     *           application/json:
     *             schema:
     *               type: object
     *               properties:
     *                 id:
     *                   type: integer
     *                 firstName:
     *                   type: string
     *                 lastName:
     *                   type: string
     *                 email:
     *                   type: string
     *                 admin:
     *                   type: boolean
     *       404:
     *         description: Użytkownik nie znaleziony.
     *       500:
     *         description: Błąd serwera.
     */
    router.get('/:id', async (req, res) => {
        try {
            const user = await User.findByPk(req.params.id);

            if (!user) {
                return res.status(404).json({ error: 'Użytkownik nie znaleziony' });
            }

            res.status(200).json(user);
        } catch (err) {
            res.status(500).json({ error: 'Błąd serwera: ' + err.message });
        }
    });

    return router;
};
