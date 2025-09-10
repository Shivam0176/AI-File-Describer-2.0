import nltk
from rake_nltk import Rake

text = '''
Thedigital marketing landscape includes
 various platforms, strategies, tools, and
 technologies that marketers use online.
 • "Landscape" here refers to the complete
 picture or ecosystem of digital marketing. It
 shows how different parts like SEO, social 
media, email, mobile apps, and analytics work
 together in the online marketing.
1. Digital marketing consists of different channels such as search 
engines, social media, mobile marketing, in fluencer marketing, 
digital PR, etc. 
• Search engine marketing done either through paid advertising or 
through search engine optimization (SEO) is good for customer 
acquisition. You may be wondering why. This is because search 
engines capture the intent of the user, and hence are more of pull 
medium, thus getting higher CTR and conversion rates than other 
media. 
• The user is interested in finding out information about a product or 
service, and is hence typing a query on the search engine. This user 
is more likely to click and take the desired action.
2. Popular portals and websites such as Yahoo!, India 
times and YouTube are very good for brand building. 
Do you know why? This is because the first step in 
brand building is creating awareness. These websites or 
mobile applications have millions of unique users and 
page views per month, and hence have a huge reach. If 
you place a banner ad on these websites, it will reach a 
large number of users, thus creating awareness. A 
standard banner ad is more like a push medium, unless 
it is remarketing to visitors of the website or doing 
behavioural targeting.
3. Social media is very apt for customer engagement as it is 
about building a community and nurturing a bond with members. 
It is not so apt for generating sales or conversions as users do not 
come to social media to buy products or services but to engage 
with friends. Marketers sometimes are disappointed that they are 
not getting enough leads or conversions from social media. They 
must understand that each medium of digital marketing has its 
own unique strengths and characteristics, and hence marketing 
objectives must be aligned to each medium's unique 
characteristics.
4.Microblogging platforms such as Twitter are apt for 
disseminating information rapidly. They are more 
about "what's happening now?" They are good for 
trending and for spreading word of mouth. This is 
because they are open networks where users can follow 
anyone without seeking any permission and one can 
view tweets of any other user even without following 
the user. The 280-character limit makes it easy for the 
user to share current events and happenings.
5.Another strategic area of digital marketing is 'online 
reputation management (ORM), which is about listening 
and understanding consumer sentiments and proactively 
shaping the brand attitude. 
Many social listening tools such as Radian 6 and Simplify 360 
identify the influencers, brand associations and sentiments. 
Another aspect of ORM is the digital PR, which is fast 
replacing the traditional PR. Many newswires have come up 
online where marketers can submit news for dissemination to 
different media and journalists, 
• Influencer marketing is another important area as in the 
digital world anybody can be an influencer, Identifying 
influencers, building relations and seeding content with 
them requires an understanding of the process.
6.Digital marketing generates a lot of digital analytics 
and metrics. Measurability is one of the strengths of 
digital marketing. Looking at the metrics and 
improvising on your digital marketing strategy helps in 
improving the ROI. Many tools are available for digital 
analytics through which the performance of each 
campaign can be measured and optimized.

 '''

def Keyword_Extractor(text):
    r = Rake()

    for resource in ["punkt", "punkt_tab"]:
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)

    r.extract_keywords_from_text(text)

    ranked_phrases = r.get_ranked_phrases()
    print("\nTop 10 Ranked Phrases(Keywords) are:\n")
    keywords = ranked_phrases[:10]

    for keyword in keywords:
        print(keyword)

    return keywords

if __name__ == "__main__":
    Keyword_Extractor(text)


