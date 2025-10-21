1. Achievements in relation to objectives 

![[IMG_7414.jpeg]]

2. Precision in our operations, risk management and controls 

3. Values and Mindset behaviours demonstrated (check notes)

---

## My Objectives - The What (achievements)

**Disclaimer: These goals were set within the first few weeks of joining the team due to my rotation on the graduate scheme.**

1 = Check in with 2-3 clients I have worked with to support - understand their app and why it's hosted on BCP
- Resolved 437+ JIRAs this year, frequently connecting with repeat customers to support them on new issues.  
- Supported ServiceMesh - resolving P3 incident by working with RedHat, ServiceMesh, and application team to troubleshoot connectivity issues. We understood that it was a bug on the RedHat side, so followed through with them to resolve this. 
- Supporting with Evergreening project for Hackathon. Mentoring and supporting the customer and their team to better understand OpenShift, and how to 

2 = Update documentation (old areas)
- SSH fix for cluster upgrades (with a link!)
- Common customer issues - a document created by a colleague to capture the most frequently seen issues, and how we can resolve them effectively.
- Created trainings for Claire/Christian on BCP knowledge. Aimed for people who are not from technical areas to better understand the platform and how it works. Created markdown slides and content to share with them and the wider team. 

3 = Work with 5+ clients for BCP 2.0 benefits 
- Worked with multiple customers to help them transition to new engineering models (eg. moving away from rolebinding groups to groups managed by enterprise breakglass)
- Still work in progress..! 

4 = Contribute to BCP 2.0 documentation 
- Goal has slightly changed since I have been focusing more on engineering and ITOps within BCP1.0, and still improving my own knowledge of BCP2.0... 

5 = Look into MLOps for BCP
- Attended session by RedHat (17/10/2025) on the new AI-powered features that are arriving in the next version. 


**MY OVERALL ACHIEVEMENTS:**
This year, I have successfully resolved 437+ customer issues via JIRA. These are often highly involved and require a conversation with the customer over MS Teams, to troubleshoot the issue and investigate to find a root cause. 

Whilst monitoring the platform (within the ITOps Alerting monitoring), I frequently identify areas where we can permanently resolve issues. 
- MultipleContainersOOMKilled - I identified the issue, and used our GitOps tools to resolve the issue for the platform.
- Customers using a high number of repliacasets - I'm currently in the process of developing a housekeeping script to resolve this issue permanently. 
- Creating RedHat cases, and working with them to resolve recurring issues. Then pulling in all necessary stakeholders to ensure we reach a conclusion - eg. etcdGRPCRequestsSlow, SDN-OVN routing bug, cluster node issues with mounting. 

Supported development of APT/BCP Calendar Automation - Automating the planning of calendar events. Although other priorities came along, I worked significantly on the development of a new tool to reduce manual work when it comes to BCP changes (in ServiceFirst). 

Troubleshooted and developed solution for loss of SSH access to master nodes post cluster upgrade - I first developed a temporary solution to backup the SSH keys during OpenShift cluster upgrades, then implemented a solution by deploying a new machine config as per a suggestion that I discussed with RedHat. I documented this so that others could repeat the process during upgrades, to ensure platform resiliency. 

Worked with major BCP stakeholders - BVP, RedHat, Networks, Storage to resolve alerts seen on the BCP Platform. I worked with multiple stakeholders around the bank, that interact with BCP to resolve alerts seen on the platform. For instance, I have carried forward an alert that we've been seeing for many months, etcdGRPCRequestsSlow which requires input from RedHat, Networks, and the BVP team, to try and work together and find a solution. I did well here in bringing people together to collaborate and resolve this issue. 

Overtime and on-call support throughout the year - I react to and resolve unforeseen events/incidents for customers, sometimes in the early hours of the morning. This requires high attention to detail, and a strong problem-solving, analytical, and methodical approach to ensure resiliency and mitigate risk on the platform. 

Cluster upgrades and maintenance - I support frequent cluster upgrades and maintenance, ensuring the platform is stable for customers and the bank, to show my dedication to risk and controls within Barclays. 

Supporting the Evergreening high-profile Hackathon project - mentoring and supporting the customer as well as their team to better understand what OpenShift is, how to use it, and how to create a resilient and highly-available app.  

GAIN Comms & Governance Co-Lead - I've served as the Comms Co-Lead, managing a team of 12 since April this year. It's been an incredible experience and has significantly developed my confidence and ability to lead others. I hold regular 121s, check in with the team, ensure that I'm giving everyone the opportunities they deserve for personal and professional growth, and co-leading a great team! 
In the role, I work closely with the GAIN Co-Chairs and our HR contacts who support early careers programmes globally. We have a rigid process for sending out comms to our GAIN members (~5000 members globally), to demonstrate my attention to detail, and proactive skill. Within the role, I also am leading on the creation of a new Ambassador Hub, the Onboarding and Offboarding of ambassadors within GAIN, a sentiment survey to check with all ambassadors how they are finding the experience - and whether we can improve it in any way, an ambassador newsletter, a member newsletter, the creation of a new GAIN website, the delivery of GAIN global pull up banners, in addition to a host of ad-hoc governance tasks to mitigate any risk to GAIN's reputation. 

Aspen Leadership, UK Rising Leaders - In April, I took part in a 2-day Leadership training, which was unlike anything I've done before. I worked with a group of 15-20 others to work out what effective leadership looked like, and how we could create organisations that thrive through personal and organisational values. 

Barclays Branch Day Visit - Earlier this year, I visited multiple Manchester Barclays' branches to see how they worked with customers, managed complaints, liquidity of the branches, networking with the customer-facing colleagues. It was really insightful to see the front-office facing role that they had, which was hugely different to my role within technology. 

Presented as a panellist for a mentorship event to 100+ colleagues - In September, I was a panellist with 2 colleagues (VP/Director) for Mentoring during careers week. We answered a host of questions from the coordinator, and the audience for 1 hour with 100+ colleagues listening in. It was a brilliant experience for me to improve my public speaking, and get outside my comfort zone! 

Fireside chat with Louisa Chapple - In September, I co-hosted a fireside chat alongside Anjali Chorlton to speak with Louisa Chapple, a new Barclays Group ExCo ex officio member. We held an interview for 1 hour alternating with questions and answering questions from the audience to an audience of 150+. She shared some incredible insights about her progression from Graduate to Managing Director at Barclays.    

Launched GTIS/CTO EC Town Hall - In October, we hosted an Early Careers Townhall for GTIS & CTO. This was the first ever one, which went really well. I collaborated with 4 others to organise the event, without support from Anjali Chortlon and Immogen Roe. The feedback was really positive, and the event was recognised globally - by colleagues in the US too. Again, this was a chance to practice my public speaking, as well as event-organising skills, and liaising with a range of people to ensure all bookings and logistics could work at the Radbroke site. 

Radbroke Speakers Group - In May, I joined the Radbroke Speakers club, created by Caspar Braithwaite who is an award-winning trainer. I've become a respected member of the club, and have delivered multiple speeches to improve my own public speaking, in addition to providing others with feedbacks and evaluations for themselves. 

---

**Specific to precision in operations, risk management, and controls:**
1. OpenShift Cluster upgrades, maintenance work and changes
2. On-Call Support, Implementation of Emergency CRs, support over Triages, and Incidents for proactive resolution
3. Alert monitoring for BCP using Grafana and bcptools 
4. Monitoring the JIRA queue to ensure customers are responded to ASAP 
5. Monitoring the BCP channels to work closely with customers, and identify any areas for resolution
6. Serving as UK Regional lead for observability to ensure we have a view of any recurring or common errors (eg. PTASK for BLB observability)
7. Completed mandatory trainings in a timely fashion 
8. Realised I made a mistake on Service First relating to change management, took full accountability, and ensured I retrained myself on the fundamentals to mitigate risk for future. 

---

**Mission - Challenge**
This year, I successfully resolved over 437 customer issues via JIRA. Many of these were complex and required detailed troubleshooting conversations over MS Teams to identify root causes. While monitoring the platform via ITOps alerting, I frequently identified problems that could be permanently fixed, such as the MultipleContainersOOMKilled issue, which I resolved using GitOps tools. I am currently developing a housekeeping script to manage customers using a high number of replica sets. I have also created cases with RedHat and worked collaboratively with all stakeholders to resolve recurring problems, including etcdGRPCRequestsSlow, SDN-OVN routing bug, and cluster node mounting issues.

**Mindset - Challenge**
I questioned existing approaches and pursued automation by supporting the development of the APT/BCP Calendar Automation to reduce manual workload in managing BCP changes within ServiceFirst. Although other priorities delayed full implementation, I contributed far along in this area. I also troubleshooted the loss of SSH access to master nodes after cluster upgrades, devising a temporary key backup solution and then implementing a machine config fix after collaborating with RedHat. This was documented thoroughly to ensure others can reproduce the fix for platform resiliency.

**Mindset - Drive**
I worked closely with major BCP stakeholders like BVP, RedHat, Networks, and Storage teams to tackle platform alerts collaboratively. This includes activities such as managing the longstanding etcdGRPCRequestsSlow alert by coordinating cross-team efforts. I provided overtime and on-call support to resolve unplanned incidents, often during overnight hours, demonstrating dedication, strong attention to detail, and methodical problem-solving to maintain platform integrity. I also supported frequent cluster upgrades and maintenance, ensuring stable and reliable services aligned with Barclays' risk and control commitments.

**Mindset - Empower**
I supported the high-profile Evergreening Hackathon project by mentoring the customer and their team, helping them understand OpenShift and how to deploy resilient, highly available applications. Additionally, as GAIN Comms & Governance Co-Lead managing a team of 12 since April, I held regular 121s, ensured team growth opportunities, and co-led initiatives. My role includes close collaboration with GAIN Co-Chairs and HR to manage early careers programmes globally, maintain rigorous communications processes to ~5000 members, and lead the creation of an Ambassador Hub, onboarding/offboarding processes, sentiment surveys, newsletters, website creation, and governance tasks mitigating reputation risks.

**Values - Respect**
I demonstrated respect by bringing together multiple stakeholders across Barclays to collaborate effectively on platform issues and by working closely with various teams and customers, treating everyone with dignity. My visit to several Barclays branches provided valuable insight into client-facing operations, enriching my appreciation for diverse roles within the bank.

**Values - Integrity**
I openly acknowledged and took full accountability for a mistake related to change management in Service First and retrained myself on fundamental processes to prevent recurrence, showing a commitment to transparency and upholding control standards.

**Values - Service**
Providing high-quality service was evident in promptly resolving JIRA tickets, actively monitoring customer communication channels and alert systems, and developing documentation and automated solutions to improve service reliability. I also helped customers upskill on BCP tools to empower self-service.

**Values - Excellence**
I displayed excellence by persistently troubleshooting critical issues, including cluster upgrades resilience through SSH key fixes, and actively participating in leadership training (Aspen Leadership, UK Rising Leaders), mentorship events, and giving talks. Joining the Radbroke Speakers Club further helped me refine my communication and public speaking skills, contributing to personal and organizational excellence.

**Values - Stewardship**
I contributed to platform stewardship through comprehensive documentation enabling repeatable maintenance steps and long-term automation projects like the replica housekeeping script. My work encourages sustainable operations and continuous improvement within Barclays.

**LEAD - Listen and be Authentic**
In my leadership roles such as the GAIN Comms Co-Lead and public-facing panels, I maintained an open, transparent approach. I routinely checked in with team members and stakeholders for feedback. I also co-hosted a fireside chat with Louisa Chapple, fostering authentic conversations about leadership and career growth.

**LEAD - Energise and Inspire**
I led events such as the GTIS/CTO Early Careers Town Hall, which received global recognition, invigorating the early careers community. Presenting at large mentorship events and engaging in fireside chats helped inspire colleagues. I also lead the creation of engaging newsletters and governance tasks within GAIN that support and energize the community.

**LEAD - Align across the Enterprise**
I aligned closely to Barclays strategy and operations by collaborating with multiple internal teams and pushing forward enterprise solutions. Managing global communications workflows and governance initiatives for the GAIN programme exemplifies my ability to deliver aligned, impactful results.

**LEAD - Develop Others**
I actively developed others through mentoring in the Evergreening Hackathon, guiding my GAIN team, contributing at mentorship panels, and providing feedback within the Radbroke Speakers group, nurturing a learning culture and supporting professional growth across the enterprise.


---

## UPDATED VERSION

---

## Mission - Challenge

This year, I successfully resolved 437+ customer issues via JIRA. These are often highly involved and require a conversation with the customer over MS Teams to troubleshoot the issue and investigate to find a root cause. I've worked with major BCP stakeholders including BVP, RedHat, Networks, and Storage to resolve alerts seen on the BCP platform. For instance, I carried forward an alert we've been seeing for many months, etcdGRPCRequestsSlow, which requires input from RedHat, Networks, and the BVP team. I did well here in bringing people together to collaborate and resolve this issue. I troubleshot and developed a solution for loss of SSH access to master nodes post cluster upgrade—first developing a temporary solution to backup SSH keys during OpenShift cluster upgrades, then implementing a permanent solution by deploying a new machine config as per a suggestion discussed with RedHat. I documented this so that others could repeat the process during upgrades to ensure platform resiliency.

## Mindset - Challenge

Whilst monitoring the platform within ITOps Alerting monitoring, I frequently identify areas where we can permanently resolve issues. I identified the MultipleContainersOOMKilled issue and used our GitOps tools to resolve it for the platform. I'm currently developing a housekeeping script to permanently resolve customers using a high number of replicasets. I create RedHat cases and work with them to resolve recurring issues, then pull in all necessary stakeholders to ensure we reach a conclusion—for example, etcdGRPCRequestsSlow, SDN-OVN routing bug, and cluster node issues with mounting. I supported development of APT/BCP Calendar Automation, automating the planning of calendar events. Although other priorities came along, I worked significantly on the development of a new tool to reduce manual work when it comes to BCP changes in ServiceFirst.

## Mindset - Drive

I provided overtime and on-call support throughout the year, reacting to and resolving unforeseen events/incidents for customers, sometimes in the early hours of the morning. This requires high attention to detail and a strong problem-solving, analytical, and methodical approach to ensure resiliency and mitigate risk on the platform. I support frequent cluster upgrades and maintenance, ensuring the platform is stable for customers and the bank, demonstrating my dedication to risk and controls within Barclays.

## Mindset - Empower

I supported the Evergreening high-profile Hackathon project, mentoring and supporting the customer as well as their team to better understand what OpenShift is, how to use it, and how to create a resilient and highly-available app. I've served as the GAIN Comms & Governance Co-Lead, managing a team of 12 since April this year. It's been an incredible experience and has significantly developed my confidence and ability to lead others. I hold regular 121s, check in with the team, ensure that I'm giving everyone the opportunities they deserve for personal and professional growth, and co-lead a great team. Within the role, I lead on the creation of a new Ambassador Hub, the onboarding and offboarding of ambassadors within GAIN, a sentiment survey to check with all ambassadors how they are finding the experience and whether we can improve it in any way, an ambassador newsletter, a member newsletter, the creation of a new GAIN website, the delivery of GAIN global pull-up banners, in addition to a host of ad-hoc governance tasks to mitigate any risk to GAIN's reputation.

## Values - Respect

Earlier this year, I visited multiple Manchester Barclays branches to see how they worked with customers, managed complaints, liquidity of the branches, and networked with the customer-facing colleagues. It was really insightful to see the front-office facing role that they had, which was hugely different to my role within technology. I worked with major BCP stakeholders—BVP, RedHat, Networks, Storage—to resolve alerts seen on the BCP Platform. I worked with multiple stakeholders around the bank that interact with BCP to resolve alerts seen on the platform.

## Values - Integrity

In the role of GAIN Comms & Governance Co-Lead, I work closely with the GAIN Co-Chairs and our HR contacts who support early careers programmes globally. We have a rigid process for sending out comms to our GAIN members (~5000 members globally), to demonstrate my attention to detail and proactive skill.

## Values - Service

This year, I successfully resolved 437+ customer issues via JIRA. These are often highly involved and require a conversation with the customer over MS Teams to troubleshoot the issue and investigate to find a root cause. I provided overtime and on-call support throughout the year, reacting to and resolving unforeseen events/incidents for customers, sometimes in the early hours of the morning.

## Values - Excellence

I troubleshot and developed a solution for loss of SSH access to master nodes post cluster upgrade—first developing a temporary solution to backup the SSH keys during OpenShift cluster upgrades, then implementing a permanent solution by deploying a new machine config as per a suggestion discussed with RedHat. I documented this so that others could repeat the process during upgrades to ensure platform resiliency. I supported development of APT/BCP Calendar Automation, automating the planning of calendar events. Although other priorities came along, I worked significantly on the development of a new tool to reduce manual work when it comes to BCP changes in ServiceFirst.

## Values - Stewardship

I support frequent cluster upgrades and maintenance, ensuring the platform is stable for customers and the bank, demonstrating my dedication to risk and controls within Barclays. Whilst monitoring the platform within ITOps Alerting monitoring, I frequently identify areas where we can permanently resolve issues, such as MultipleContainersOOMKilled which I resolved using our GitOps tools, and developing a housekeeping script for customers using a high number of replicasets.

## LEAD - Listen and be Authentic

In April, I took part in a 2-day Aspen Leadership UK Rising Leaders training, which was unlike anything I've done before. I worked with a group of 15-20 others to work out what effective leadership looked like and how we could create organisations that thrive through personal and organisational values. I hold regular 121s with my GAIN team, check in with the team, and ensure that I'm giving everyone the opportunities they deserve for personal and professional growth.

## LEAD - Energise and Inspire

In September, I was a panellist with 2 colleagues (VP/Director) for a mentorship event during careers week to 100+ colleagues. We answered a host of questions from the coordinator and the audience for 1 hour. It was a brilliant experience for me to improve my public speaking and get outside my comfort zone. In September, I co-hosted a fireside chat alongside Anjali Chorlton to speak with Louisa Chapple, a new Barclays Group ExCo ex officio member. We held an interview for 1 hour alternating with questions and answering questions from the audience to an audience of 150+. She shared some incredible insights about her progression from Graduate to Managing Director at Barclays. In October, we hosted the first ever Early Careers Town Hall for GTIS & CTO, which went really well. I collaborated with 4 others to organise the event with support from Anjali Chorlton and Immogen Roe. The feedback was really positive, and the event was recognised globally by colleagues in the US too. This was a chance to practice my public speaking as well as event-organising skills and liaising with a range of people to ensure all bookings and logistics could work at the Radbroke site.

## LEAD - Align across the Enterprise

I worked with major BCP stakeholders—BVP, RedHat, Networks, Storage—to resolve alerts seen on the BCP Platform. I worked with multiple stakeholders around the bank that interact with BCP to resolve alerts seen on the platform. For instance, I carried forward an alert we've been seeing for many months, etcdGRPCRequestsSlow, which requires input from RedHat, Networks, and the BVP team to try and work together and find a solution. In the GAIN Comms & Governance Co-Lead role, I work closely with the GAIN Co-Chairs and our HR contacts who support early careers programmes globally. We have a rigid process for sending out comms to our GAIN members (~5000 members globally).

## LEAD - Develop Others

I supported the Evergreening high-profile Hackathon project, mentoring and supporting the customer as well as their team to better understand what OpenShift is, how to use it, and how to create a resilient and highly-available app. As GAIN Comms & Governance Co-Lead managing a team of 12 since April this year, I hold regular 121s, check in with the team, and ensure that I'm giving everyone the opportunities they deserve for personal and professional growth. In May, I joined the Radbroke Speakers club created by Caspar Braithwaite, who is an award-winning trainer. I've become a respected member of the club and have delivered multiple speeches to improve my own public speaking, in addition to providing others with feedback and evaluations for themselves.

---

## Areas for Attention

No significant low areas identified. All values and mindsets are well-demonstrated through comprehensive technical contributions, leadership initiatives, and stakeholder engagement.

---

This detailed mapping provides your manager with a full view of your achievements and how they align with Barclays' Values and Mindset framework.

1. [https://www.indeed.com/career-advice/career-development/self-performance-review](https://www.indeed.com/career-advice/career-development/self-performance-review)
2. [https://lattice.com/articles/tips-for-writing-a-strong-self-evaluation-plus-specific-examples-to-make-yours-shine](https://lattice.com/articles/tips-for-writing-a-strong-self-evaluation-plus-specific-examples-to-make-yours-shine)
3. [https://www.teammaven.io/blog/self-evaluation-examples-60-of-the-best-sample-answers-for-employees-and-managers](https://www.teammaven.io/blog/self-evaluation-examples-60-of-the-best-sample-answers-for-employees-and-managers)
4. [https://www.qualtrics.com/en-gb/experience-management/employee/employee-self-evaluation/](https://www.qualtrics.com/en-gb/experience-management/employee/employee-self-evaluation/)
5. [https://www.deel.com/blog/self-evaluation-examples/](https://www.deel.com/blog/self-evaluation-examples/)
6. [https://www.highspeedtraining.co.uk/hub/how-to-write-a-self-evaluation/](https://www.highspeedtraining.co.uk/hub/how-to-write-a-self-evaluation/)
7. [https://hbr.org/2023/12/how-to-write-an-effective-self-assessment](https://hbr.org/2023/12/how-to-write-an-effective-self-assessment)
8. [https://www.reddit.com/r/cscareerquestions/comments/1g8jtbi/how_do_you_write_a_self_review_of_your/](https://www.reddit.com/r/cscareerquestions/comments/1g8jtbi/how_do_you_write_a_self_review_of_your/)
9. [https://www.linkedin.com/pulse/how-do-i-write-up-my-self-review-performance-review-time-svilpa-4jeie](https://www.linkedin.com/pulse/how-do-i-write-up-my-self-review-performance-review-time-svilpa-4jeie)
10. [https://www.peoplebox.ai/blog/self-evaluation-examples/](https://www.peoplebox.ai/blog/self-evaluation-examples/)