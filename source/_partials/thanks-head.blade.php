<title>{{ $page->title }}</title>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="content-language" content="{{ $page->lang }}">
<meta charset="{{ $page->head->charset }}">
<meta name="viewport" content="{{ $page->head->viewport }}">
<meta name="robots" content="{{ $page->head->robots }}">
<meta name="description" content="{{ $page->head->description }}">
<meta name="keywords" content="{{ $page->head->keywords }}" />
<meta name="author" content="{{ $page->head->author }}">
<meta name="google-site-verification" content="{{ $page->head->google_site_verification }}">
<meta name="og:title" property="og:title" content="{{ $page->title }}" />
<meta name="og:type" property="og:type" content="{{ $page->head->og_type }}" />
<meta name="og:site_name" property="og:site_name" content="{{ $page->title }}" />
<meta name="og:description" property="og:description" content="{{ $page->description }}" />
<meta name="og:url" property="og:url" content="{{ $page->head->og_url }}" />
<meta name="og:image" property="og:image" content="{{ $page->head->og_image }}" />
<meta name="fb:app_id" property="fb:app_id" content="{{ $page->head->fb_app_id }}" />
<meta name="twitter:card" property="twitter:card" content="{{ $page->head->twitter_card }}" />
<meta name="twitter:site" property="twitter:site" content="{{ $page->head->twitter_site }}" />
<meta name="twitter:title" property="twitter:title" content="{{ $page->title }}" />
<meta name="twitter:description" property="twitter:description" content="{{ $page->description }}" />
<meta name="twitter:url" property="twitter:url" content="{{ $page->head->twitter_url }}" />
<meta name="twitter:image" property="twitter:image" content="{{ $page->head->twitter_image }}" />
<link rel="shortcut icon" href="images{{ $page->icon }}" type="image/x-icon">
<link rel="stylesheet" href="../css/big-picture.min.css" />
<!-- [if lte IE 8 ]]> <script src="js/ie/html5shiv.js"></script><![endif] -->
<!--[if lte IE 8]><link rel="stylesheet" href="css/ie8.css" /><![endif]-->
<!--[if lte IE 8]><link rel="stylesheet" href="css/ie9.css" /><![endif]-->