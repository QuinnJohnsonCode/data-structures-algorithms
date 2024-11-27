import styles from './footer.module.css';

const Footer = () => {
    return (
        <div className={styles.container}>
            <div className={styles.logo}>quinn</div>
            <div className={styles.text}>
                Copyright © 2024 All Rights Reserved
            </div>
        </div>
    );
};

export default Footer;