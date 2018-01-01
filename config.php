<?php

return [
    'baseUrl' => '',
    'production' => false,
    'collections' => [],

    'title' => 'Stifix',
    'email' => 'stifan.kristi@stifix.com',
    'description' => 'Stifix Company Profile Website',
    'lang' => 'en',
    'icon' => '/favicon.ico',

    'head' => [
    	'charset' => 'utf-8',
    	'viewport' => 'width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no',
   		'robots' => 'all',
   		'description' => 'Stifix Company Profile Website',
   		'keywords' => 'Stifix, IT, IT Services, IT Solutions, IT Security, IT Monitoring, IT Development, IT Maintenance, IT Configuration, IT Support, IT Installation, IT Upgrade, IT Analyst, IT Development, IT Testing, System, System Services, System Solutions, Security System, Monitoring System, System Development, Maintenance System, Configuration System, System Support, Installation System, Upgrade System, System Analyst, System Development, Testing System, Linux, Unix, Windows, Virtualization, Cloud Computing, Mobile, Web Development',
   		'author' => 'Stifan Kristi',
    	'google_site_verification' => 'ibaNUNECBXNjZi_FDdbSRZv9nIhCdZsJQ6n27Qfv1Tk',
    	'og_type' => 'website',
   		'og_url' => 'http://stifix.com',
   		'og_image' => 'http://stifix.com',
   		'fb_app_id' => 'stifixid',
   		'twitter_card' => 'summary',
    	'twitter_site' => '@stifixid',
    	'twitter_url' => 'http://stifix.com',
   		'twitter_image' => 'http://stifix.com',
    ],

    'header' => [
    	[
    		'link' => '#intro',
    		'title' => 'Intro',
    	],
    	[
    		'link' => '#who_we_are',
    		'title' => 'Who We Are',
    	],
    	[
    		'link' => '#what_we_do',
    		'title' => 'What We Do',
    	],
    	[
    		'link' => '#why_us',
    		'title' => 'Why Us',
    	],
    	[
    		'link' => '#contact',
    		'title' => 'Contact',
    	],
    ],

    'intro' => [
      'title' => 'Welcome',
      'description' => 'We provide comprehensive IT services and solutions to our clients based on their demands with effective, efficient and economic solutions.',
      'buttontext' => 'More',
      'buttonlink' => '#who_we_are',
      'picture' => 'intro.jpg',
    ],

    'who_we_are' => [
      'title' => 'Who We Are',
      'description' => 'We set out to giving IT services and solutions since 2000, start to those around us, and we keep growing and fruitful to help more people by solving their IT problems.',
      'buttontext' => 'next',
      'buttonlink' => '#what_we_do',
      'picture' => 'who_we_are.jpg',
    ],

    'what_we_do' => [
      'title' => 'What We Do',
      'description' => 'Our services and solutions includes Installation, Configuration, Upgrades, Support, Training, Monitoring, Maintenance, and Development. We deliver according to your request.',
      'buttontext' => 'next',
      'buttonlink' => '#why_us',
      'picture' => 'what_we_do.jpg',
    ],

    'why_us' => [
      'title' => 'Why Us',
      'description' => 'Experienced in IT Industry for a long time and always up to date with the recent technology, and the most important thing, we care to you by solving your IT problems.',
      'buttontext' => 'next',
      'buttonlink' => '#footer',
      'picture' => 'why_us.jpg',
    ],

    'contact' => [
      'title' => 'Tell us your IT Problem',
      'description' => 'We are going to listening you and reach you as soon as possible.',
    ],

    'home_footer' => [
      'list' => [
        [
          'title' => 'Facebook',
          'icon' => 'fa-facebook',
          'link' => 'https://facebook.com/stifixid',
        ],
        [
          'title' => 'Twitter',
          'icon' => 'fa-twitter',
          'link' => 'https://twitter.com/stifixid',
        ],
        [
          'title' => 'Google Plus',
          'icon' => 'fa-google-plus',
          'link' => 'https://plus.google.com/+Stifix',
        ],
        [
          'title' => 'Email',
          'icon' => 'fa-envelope',
          'link' => 'mailto:stifan.kristi@stifix.com',
        ],
      ],
      'copyright' => '© 2017 stifix. All rights reserved.',
    ],

    'thanks' => [
      'title' => 'Thank you',
      'description' => 'Thank you for contacting us.<br/>We are going to response your message as soon as possible.',
      'buttontext' => 'Back To Home Page',
      'list' => [
        [
          'icon' => 'fa-linux',
        ],
        [
          'icon' => 'fa-apple',
        ],
        [
          'icon' => 'fa-windows',
        ],
        [
          'icon' => 'fa-mobile',
        ],
        [
          'icon' => 'fa-laptop',
        ],
        [
          'icon' => 'fa-desktop',
        ],
        [
          'icon' => 'fa-server',
        ],
        [
          'icon' => 'fa-cloud',
        ],
      ],
    ],

    'resume_header' => [
      'name' => 'Stifan Kristi',
      'occupation' => 'IT Consultant',
      'address' => 'Kacang Polong 3 No 18',
      'city' => 'Jakarta',
      'country' => 'Indonesia',
      'list' => [
        [
          'title' => 'stifan.kristi@stifix.com',
          'icon' => 'fi-mail',
          'link' => 'mailto:stifan.kristi@stifix.com',
        ],
        [
          'title' => '+62818783118',
          'icon' => 'fi-mobile',
          'link' => 'tel:+62818783118',
        ],
        [
          'title' => '+6285888607267',
          'icon' => 'fi-mobile',
          'link' => 'tel:+6285888607267',
        ],
        [
          'title' => 'stifix.com',
          'icon' => 'fi-web',
          'link' => 'https://stifix.com',
        ],
      ],
    ],

    'objective' => [
      'title' => 'Objective',
      'description' => 'Aspire to contribute to solve the problem and make daily operational more effective, efficient, economic and sustainable, both individually and as part of a team',
    ],

    'specialities' => [
      'title' => 'Specialities',
      'list' => [
        [
          'title' => 'Various Hardware',
          'icon' => 'fi-laptop',
          'animated' => 'fadeInDown',
        ],
        [
          'title' => 'Various Environment',
          'icon' => 'fi-cloud',
          'animated' => 'fadeInUp',
        ],
        [
          'title' => 'Various OS',
          'icon' => 'fi-social-windows',
          'animated' => 'fadeInLeft',
        ],
      ],
    ],

    'computer_skills' => [
      'title' => 'Computer Skills',
      'list' => [
        [
          'title' => '1. Computer',
        ],
        [
          'title' => '2. Management',
        ],
      ],
    ],

    'language_skills' => [
      'title' => 'Language Skills',
      'list' => [
        [
          'title' => 'Indonesian',
          'level' => 'Mother Language',
        ],
        [
          'title' => 'English',
          'level' => 'Advanced Level',
        ],
        [
          'title' => 'Japanese',
          'level' => 'Basic Level',
        ],
      ],
    ],

    'recognitions' => [
      'title' => 'Recognitions',
      'position' => '1-3',
      'recognitions' => 'Bina Nusantara Scholarship',
      'description' => 'Academic Performance in Bina Nusantara University',
      'place' => 'Bina Nusantara University, Indonesia',
    ],

    'experience' => [
      'title' => 'Experience',
      'year' => '4',
      'date' => 'From 2013 to now',
      'role' => 'IT Consultant',
      'company' => 'Stifix',
    ],

    'education' => [
      'title' => 'Education',
      'date' => 'From 2002 to 2006',
      'topic' => 'Computerized Accounting',
      'school' => 'Bina Nusantara University, Indonesia',
    ],

    'hobbies_interest' => [
      'title' => 'Hobbies & Interests',
      'list' => [
        [
          'title' => 'Photography',
          'icon' => 'fi-camera',
        ],
        [
          'title' => 'Nature',
          'icon' => 'fi-mountains',
        ],
        [
          'title' => 'Reading',
          'icon' => 'fi-book',
        ],
        [
          'title' => 'Music',
          'icon' => 'fi-music',
        ],
        [
          'title' => 'Travelling',
          'icon' => 'fi-trees',
        ],
        [
          'title' => 'Pets',
          'icon' => 'fi-paw',
        ],
        [
          'title' => 'Games',
          'icon' => 'fi-die-six',
        ],
        [
          'title' => 'Theatre',
          'icon' => 'fi-ticket',
        ],
      ],
    ],

    'resume_footer' => [
      'name' => 'Stifan Kristi',
      'link' => 'mailto:stifan.kristi@stifix.com',
    ],

];
