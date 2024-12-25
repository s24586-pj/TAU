import swaggerJSDoc from 'swagger-jsdoc';

const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'API Documentation',
            version: '1.0.0',
            description: 'Swagger do endpointów',
        },
        servers: [
            {
                url: 'http://localhost:3000',
                description: 'Swagger server',
            },
        ],
    },
    apis: ['./router/*.js'],
};

const swaggerSpec = swaggerJSDoc(options);

export default swaggerSpec;
