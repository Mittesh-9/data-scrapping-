# Data Scraping

## Attack Types

### What Is Data Scraping?

Data scraping, or web scraping, is a process of importing data from websites into files or spreadsheets. It is used to extract data from the web, either for personal use by the scraping operator, or to reuse the data on other websites. There are numerous software applications for automating data scraping.

Data scraping is commonly used to:

- Collect business intelligence to inform web content
- Determine prices for travel booking or comparison sites
- Find sales leads or conduct market research via public data sources
- Send product data from eCommerce sites to online shopping platforms like Google Shopping

Data scraping has legitimate uses, but is often abused by bad actors. For example, data scraping is often used to harvest email addresses for the purpose of spamming or scamming. Scraping can also be used to retrieve copyrighted content from one website and automatically publish it on another website.

Some countries prohibit the use of automated email harvesting techniques for commercial gain, and it is generally considered an unethical marketing practice.

## Data Scraping and Cybersecurity

Data scraping tools are used by all sorts of businesses, not necessarily for malicious purposes. These include marketing research and business intelligence, web content and design, and personalization.

However, data scraping also poses challenges for many businesses, as it can be used to expose and misuse sensitive data. The website being scraped might not be aware that their data is collected, or what is being collected. Likewise, a legitimate data scraper might not store the data securely, allowing attackers to access it.

If malicious actors can access the data collected through web scraping, they can exploit it in cyber attacks. For example, attackers can use scraped data to perform:

- Phishing attacks
- Password cracking attacks

## Data Scraping Techniques

Here are a few techniques commonly used to scrape data from websites:

### HTML Parsing

HTML parsing involves the use of JavaScript to target a linear or nested HTML page. It is a powerful and fast method for extracting text and links (e.g. a nested link or email address), scraping screens and pulling resources.

### DOM Parsing

The Document Object Model (DOM) defines the structure, style and content of an XML file. Scrapers typically use a DOM parser to view the structure of web pages in depth. DOM parsers can be used to access the nodes that contain information and scrape the web page with tools like XPath. For dynamically generated content, scrapers can embed web browsers like Firefox and Internet Explorer to extract whole web pages (or parts of them).

### Vertical Aggregation

Companies that use extensive computing power can create vertical aggregation platforms to target particular verticals. These are data harvesting platforms that can be run on the cloud and are used to automatically generate and monitor bots for certain verticals with minimal human intervention. Bots are generated according to the information required to each vertical, and their efficiency is determined by the quality of data they extract.

### XPath

XPath is short for XML Path Language, which is a query language for XML documents. XML documents have tree-like structures, so scrapers can use XPath to navigate through them by selecting nodes according to various parameters. A scraper may combine DOM parsing with XPath to extract whole web pages and publish them on a destination site.

### Google Sheets

Google Sheets is a popular tool for data scraping. Scarpers can use the IMPORTXML function in Sheets to scrape from a website, which is useful if they want to extract a specific pattern or data from the website. This command also makes it possible to check if a website can be scraped or is protected.

## How to Mitigate Web Scraping

For content to be viewable, web content usually needs to be transferred to the machine of the website viewer. This means that any data the viewer can access is also accessible to a scraping bot. You can use the following methods to reduce the amount of data that can be scraped from your website.

### Rate Limit User Requests

The rate of interaction for human visitors clicking through a website is relatively predictable. For example, it is impossible for a human to go through 100 web pages per second, while machines can make multiple simultaneous requests. The rate of requests can indicate the use of data scraping techniques that attempt to scrape your entire site in a short time.

You can rate limit the number of requests an IP address can make within a particular time frame. This will protect your website from exploitation and significantly slow down the rate at which data scraping can occur.

### Mitigate High-Volume Requesters with CAPTCHAs

Another way to slow down data scraping efforts is to apply CAPTCHAs. These require website visitors to complete a task that would be relatively easy for a human but prohibitively challenging for a machine. Even if a bot can get past the CAPTCHA once, it will not be able to do so across multiple instances. The drawback of CAPTCHA challenges is their potential negative impact on user experience.

### Regularly Modify HTML Markup

A data scraping bot needs consistent formatting to be able to traverse a website and parse useful information effectively. You can interrupt the workflow of a bot by modifying HTML markup elements on a regular basis.

For example, you can nest HTML elements or change various markup aspects, which will make it more difficult to scrape consistently. Some websites implement randomized modifications whenever they are rendered, in order to protect their content. Alternatively, websites can modify their markup code less frequently, with the aim of preventing a longer-term data scraping effort.

### Embed Content in Media Objects

This is a less popular method of mitigation that involves media objects such as images. To extract data from image files, you need to use optical character recognition (OCR), as the content doesn’t exist as a string of characters. This makes the process of copying content much more complicated for data scrapers, but it can also be an obstacle to legitimate web users, who will not be able to copy content from the website and must instead retype or memorize it.

However, the above methods are partial and do not guarantee protection against scraping. To fully protect your website, deploy a bot protection solution that detects scraping bots, and is able to block them before they connect to your website or web application.

## Scraping Bot Protection with Imperva

Imperva provides Advanced Bot Protection, which prevents business logic attacks from all access points – websites, mobile apps and APIs. Gain seamless visibility and control over bot traffic to stop online fraud through account takeover or competitive price scraping.

Beyond bot protection, Imperva provides comprehensive protection for applications, APIs, and microservices:

- Web Application Firewall – Prevent attacks with world-class analysis of web traffic to your applications.
- Runtime Application Self-Protection (RASP) – Real-time attack detection and prevention from your application runtime environment goes wherever your applications go. Stop external attacks and injections and reduce your vulnerability backlog.
- API Security – Automated API protection ensures your API endpoints are protected as they are published, shielding your applications from exploitation.
- DDoS Protection – Block attack traffic at the edge to ensure business continuity with guaranteed uptime and no performance impact. Secure your on-premises or cloud-based assets – whether you’re hosted in AWS, Microsoft Azure, or Google Public Cloud.
- Attack Analytics – Ensures complete visibility with machine learning and domain expertise across the application security stack to reveal patterns in the noise and detect application attacks, enabling you to isolate and prevent attack campaigns.
- Client-Side Protection – Gain visibility and control over third-party JavaScript code to reduce the risk of supply chain fraud, prevent data breaches, and client-side attacks.
