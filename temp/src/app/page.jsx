import styles from './home.module.css';
import Image from 'next/image';

const Home = () => {
  return (
    <div className={styles.container}>
      <div className={styles.textContainer}>
        <h1 className={styles.title}>Creative Thoughts Agency.</h1>
        <p className={styles.desc}>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
          Deserunt deleniti atque, praesentium nemo amet, dolorum autem.
        </p>

        <div className={styles.buttons}>
          <button className={styles.button}>Learn More</button>
          <button className={styles.button}>Contact</button>
        </div>

        <div className={styles.brands}>
          <Image src="/brands.png" alt="Logos for Reddit/Discord/Steam/Twitch." fill className={styles.brandImg} />
        </div>
      </div>
      <div className={styles.imgContainer}>
        <Image src="/hero.gif" alt="4 people collaborating together to assemble a lightbulb that looks like a puzzle." fill className={styles.heroImg} />
      </div>
    </div>
  );
};

export default Home;