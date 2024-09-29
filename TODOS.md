# Link Organizer

In order to correctly organize the links, we need to correctly classify them into topics.
to do so, we have a few options:

- Train an AI model to classify the links into topics LDA, BERT, gensim
- Do we train the model at runtime? Where to train it? On what data?
- Do we use a combination of NLP and a predefined TOPIC_MAP?
    - NLP to classify the links into a topic
    - TOPIC_MAP to map the topic into a category

These questions are critical to making this tool useful and scalable.

At the end of the day, we need to map a link to a topic and a topic to a category.

This can already be done via manually specifying the topic of a link, and specifying the category of a topic.

# Categories and map to build LDA model

A scraper and preprocessor will be needed to extract the links and classify them into topics.
These are just some links off the top of my head. Can add more as we go.

```python
categories = {
    'programming_languages': ['python', 'javascript', 'ruby', 'cpp', 'java', 'rust', 'go', 'php', 'typescript', 'swift'],
    'devops': ['docker', 'kubernetes', 'jenkins', 'ci_cd', 'ansible', 'terraform', 'prometheus', 'infrastructure_as_code'],
    'machine_learning': ['supervised_learning', 'unsupervised_learning', 'reinforcement_learning', 'deep_learning', 'nlp'],
    'cybersecurity': ['penetration_testing', 'network_security', 'cryptography', 'incident_response', 'malware_analysis'],
    'software_development': ['agile', 'tdd', 'microservices', 'version_control', 'design_patterns'],
    'cloud_computing': ['aws', 'gcp', 'azure', 'serverless', 'cloud_security'],
    'databases': ['sql', 'nosql', 'database_optimization', 'data_warehousing'],
    'networking': ['tcp_ip', 'dns', 'http_https', 'load_balancers', 'osi_model'],
    'operating_systems': ['linux', 'windows', 'macos', 'kernel_architecture'],
    'data_science': ['data_cleaning', 'data_visualization', 'feature_engineering', 'big_data'],
    'web_development': ['frontend', 'backend', 'api_development', 'web_security', 'pwas'],
    'blockchain': ['bitcoin', 'ethereum', 'smart_contracts', 'dapps', 'consensus_algorithms'],
    'artificial_intelligence': ['expert_systems', 'nlp', 'game_ai', 'image_recognition'],
    'mobile_development': ['android', 'ios', 'cross_platform', 'mobile_security']
}
```
1. Programming Languages
- Python Documentation: https://docs.python.org/3/
- JavaScript Documentation: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- Ruby Documentation: https://ruby-doc.org/
- Rust Programming Blog: https://blog.rust-lang.org/
- Go Documentation: https://golang.org/doc/

2. DevOps
- Docker Official Documentation: https://docs.docker.com/
- Kubernetes Documentation: https://kubernetes.io/docs/
- Jenkins Documentation: https://www.jenkins.io/doc/
- Terraform Documentation: https://www.terraform.io/docs
- Ansible Documentation: https://docs.ansible.com/

3. Machine Learning
- Scikit-learn Documentation: https://scikit-learn.org/stable/
- TensorFlow Documentation: https://www.tensorflow.org/guide
- Towards Data Science Blog: https://towardsdatascience.com/
- Machine Learning Mastery Blog: https://machinelearningmastery.com/
- KDNuggets Blog: https://www.kdnuggets.com/

4. Cybersecurity
- OWASP (Open Web Application Security Project): https://owasp.org/
- Krebs on Security Blog: https://krebsonsecurity.com/
- Cybrary Blog: https://www.cybrary.it/blog/
- SANS Institute Blog: https://www.sans.org/blog/
- Hacker News: https://news.ycombinator.com/

5. Software Development
- Dev.to Blog: https://dev.to/
- Medium Software Development Topics: https://medium.com/tag/software-development
- Stack Overflow Discussions: https://stackoverflow.com/
- Martin Fowler’s Blog on Agile and Software Architecture: https://martinfowler.com/

6. Cloud Computing
- AWS Documentation: https://docs.aws.amazon.com/
- Google Cloud Documentation: https://cloud.google.com/docs/
- Azure Documentation: https://docs.microsoft.com/en-us/azure/
- CloudAcademy Blog: https://cloudacademy.com/blog/

7. Databases
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- MongoDB Documentation: https://docs.mongodb.com/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/en/14/
- DataStax Blog (for Apache Cassandra): https://www.datastax.com/blog
- AWS RDS Documentation: https://aws.amazon.com/rds/

8. Networking
- Cisco Networking Academy: https://www.netacad.com/
- Networking Tutorials by Juniper: https://www.juniper.net/us/en/learning/
- Networking Documentation from IBM: https://www.ibm.com/cloud/architecture
- RFC (Request for Comments) Documentation: https://www.rfc-editor.org/
- Arista Network Documentation: https://www.arista.com/en/

9. Operating Systems
- Linux Kernel Documentation: https://www.kernel.org/doc/html/latest/
- Arch Linux Wiki: https://wiki.archlinux.org/
- Windows Developer Blog: https://blogs.windows.com/windowsdeveloper/
- macOS Developer Documentation: https://developer.apple.com/documentation/
- Unix Stack Exchange: https://unix.stackexchange.com/

10. Data Science
- Kaggle Discussions and Blogs: https://www.kaggle.com/
- R-bloggers (R Programming Language for Data Science): https://www.r-bloggers.com/
- Towards Data Science Blog: https://towardsdatascience.com/
- DataCamp Blog: https://www.datacamp.com/community/blog
- Google AI Blog: https://ai.googleblog.com/

11. Web Development
- CSS-Tricks Blog: https://css-tricks.com/
- Smashing Magazine: https://www.smashingmagazine.com/
- Mozilla Developer Network (MDN): https://developer.mozilla.org/en-US/
- Web.dev (by Google): https://web.dev/
- FreeCodeCamp Blog: https://www.freecodecamp.org/news/

12. Blockchain
- Bitcoin Developer Documentation: https://developer.bitcoin.org/reference/
- Ethereum Documentation: https://ethereum.org/en/developers/docs/
- Hyperledger Documentation: https://hyperledger-fabric.readthedocs.io/en/latest/
- CoinDesk (Blockchain News and Analysis): https://www.coindesk.com/
- Blockchain.com Blog: https://blog.blockchain.com/

13. Artificial Intelligence
- OpenAI Blog: https://openai.com/blog/
- DeepMind Blog: https://deepmind.com/blog/
- MIT News on AI: https://news.mit.edu/topic/artificial-intelligence2
- AI Alignment Blog: https://www.alignmentforum.org/
- Facebook AI Blog: https://ai.facebook.com/blog/

14. Mobile Development
- Android Developer Blog: https://developer.android.com/news
- iOS Developer Documentation: https://developer.apple.com/documentation/
- React Native Blog: https://reactnative.dev/blog
- Flutter Blog: https://medium.com/flutter
- MobileDevMemo Blog: https://www.mobiledevmemo.com/

## General Data Processing

### Done
- [x] Add a way to add links manually
- [x] Add a way to add links from a file
- [x] Add a way to add links from a directory
- [x] Add a way to add links from a CSV file
- [x] Add a way to add links from an Excel file
- [x] Add a way to add links from a text file

### TODO
- [ ] Add a way to add links from a markdown file
- [ ] Add a way to add links from a JSON file
- [ ] Add a way to add links from a YAML file
- [ ] Add a way to add links from a XML file
- [ ] Add a way to add links from a HTML file
- [ ] Add a way to add links from a RSS feed
- [ ] Add a way to add links from a API
- [ ] Add a way to add links from a database
- [ ] Add a way to add links from a website
