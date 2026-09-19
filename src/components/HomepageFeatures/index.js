import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  { title: 'Physical AI Foundations', description: 'Learn how sensing, actuation, control, and AI connect physical systems to intelligent behavior.' },
  { title: 'Interactive Robotics Assistant', description: 'Use the built-in assistant while studying modules and exploring core humanoid-robotics concepts.' },
  { title: 'Bilingual Learning', description: 'Study the textbook in English or Urdu with the locale switcher built into the site.' },
];
function Feature({title, description}) { return <div className={clsx('col col--4')}><div className="text--center padding-horiz--md"><Heading as="h3">{title}</Heading><p>{description}</p></div></div>; }
export default function HomepageFeatures() { return <section className={styles.features}><div className="container"><div className="row">{FeatureList.map((props) => <Feature key={props.title} {...props} />)}</div></div></section>; }
