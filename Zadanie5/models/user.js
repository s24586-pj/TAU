import { DataTypes } from 'sequelize';

export default (sequelize) => {
    const User = sequelize.define('User', {
            firstName: {
                type: DataTypes.STRING,
                allowNull: false,
            },
            lastName: {
                type: DataTypes.STRING,
            },
            email: {
                type: DataTypes.STRING,
                allowNull: false,
                unique: true,
            },
            admin:{
                type: DataTypes.BOOLEAN,
                allowNull: false,
                required: false,
                defaultValue: false,
            }
        },
        {
            timestamps: false
        });

    return User;
};
