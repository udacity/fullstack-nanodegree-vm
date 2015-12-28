



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled is-u2f-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    
    
    <title>Full-Stack-Foundations/lotsofmenus.py at master · lobrown/Full-Stack-Foundations</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="lobrown/Full-Stack-Foundations" name="twitter:title" /><meta content="Full-Stack-Foundations - Solution Code to Full Stack Foundations (ud088)" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/9041401?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/9041401?v=3&amp;s=400" property="og:image" /><meta content="lobrown/Full-Stack-Foundations" property="og:title" /><meta content="https://github.com/lobrown/Full-Stack-Foundations" property="og:url" /><meta content="Full-Stack-Foundations - Solution Code to Full Stack Foundations (ud088)" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTA1ODY5NDY6YWU1YzJjNDFkNDE5YWZmNWQ2NzMwYWFiN2MzY2EyODg6ZTI0NGQ5MDVmYWUzZDRhNWVkOTBjMDE3OWI0MjI0ZjA3ZThkYjlkMTk3ZTJhOWQzZDgzNmZhMmFhMTFjZjcwMg==--f766dc534e5c1ca856cdbf6378f8762b175fc5c0">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="BAD2A84E:35CE:2DEFA90F:567DEB2A" name="octolytics-dimension-request_id" /><meta content="10586946" name="octolytics-actor-id" /><meta content="haredega" name="octolytics-actor-login" /><meta content="c7add76307e71ea7a149af39ecd60c82a04afaa859e90717e1fafcb8dd6e193f" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />
<meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />


  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="haredega">

        <meta name="expected-hostname" content="github.com">

      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta content="33cefdc1406c4a380e0f61d27043bd844daf6fb5" name="form-nonce" />

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-46ac4202cb3c472c54a367e85742188d9f18080f1a0f770de0df1718b8b6e657.css" integrity="sha256-RqxCAss8RyxUo2foV0IYjZ8YCA8aD3cN4N8XGLi25lc=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2-451ab63ad67fa9af580e5d9a3b2b7de911ce2e4b2437638f26fe8cb3879e67d8.css" integrity="sha256-RRq2OtZ/qa9YDl2aOyt96RHOLkskN2OPJv6Ms4eeZ9g=" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="31721428bbdc966faf15eae27addeadd">

      
  <meta name="description" content="Full-Stack-Foundations - Solution Code to Full Stack Foundations (ud088)">
  <meta name="go-import" content="github.com/lobrown/Full-Stack-Foundations git https://github.com/lobrown/Full-Stack-Foundations.git">

  <meta content="9041401" name="octolytics-dimension-user_id" /><meta content="lobrown" name="octolytics-dimension-user_login" /><meta content="30271096" name="octolytics-dimension-repository_id" /><meta content="lobrown/Full-Stack-Foundations" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="30271096" name="octolytics-dimension-repository_network_root_id" /><meta content="lobrown/Full-Stack-Foundations" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/lobrown/Full-Stack-Foundations/commits/master.atom" rel="alternate" title="Recent Commits to Full-Stack-Foundations:master" type="application/atom+xml">

  </head>


  <body class="logged_in   env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github "></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/lobrown/Full-Stack-Foundations/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:haredega"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
          <span class="mail-status all-read"></span>
          <span class="octicon octicon-bell "></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="lobrown/Full-Stack-Foundations">This repository</span>
  </div>
    <a class="dropdown-item" href="/lobrown/Full-Stack-Foundations/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/haredega"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@haredega" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/10586946?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu  dropdown-menu-sw">
        <div class=" dropdown-header header-nav-current-user css-truncate">
            Signed in as <strong class="css-truncate-target">haredega</strong>

        </div>


        <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/haredega" data-ga-click="Header, go to profile, text:your profile">
            Your profile
          </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>

          <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
            Settings
          </a>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="OL2As0AcKDM+lm/ukzR41Rneg4LCf8VAElXvuvCqeuaQaC0SyFw41/dQyD3LLVIJkNKjS5SA/Tgt3ToUw/wMrA==" /></div>
            <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
              Sign out
            </button>
</form>
      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

      

      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/WebPage">
    <div id="js-repo-pjax-container" class="context-loader-container js-repo-nav-next" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="4V7ail++ewpOzFufTp4qBrCd3agCx3y5/KjsK2QWtptPvTA+h45o9sZrnG0Jtewn0vGWaeIYJXbSX5R9ClW8+A==" /></div>      <input id="repository_id" name="repository_id" type="hidden" value="30271096" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/lobrown/Full-Stack-Foundations/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <span class="octicon octicon-eye "></span>
              Watch
            </span>
          </a>
          <a class="social-count js-social-count" href="/lobrown/Full-Stack-Foundations/watchers">
            15
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span aria-label="Close" class="octicon octicon-x js-menu-close" role="button"></span>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-eye"></span>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <span class="octicon octicon-mute"></span>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/unstar" class="js-toggler-form starred js-unstar-button" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Qbgz1mFGMXBxo6vYqK8LiW8Ag5sQFiVRJIeDmqPDPAFHZri688gulYHP/erKE4ND60pYcenKJWAh1WRwXq4gow==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar lobrown/Full-Stack-Foundations"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star "></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/lobrown/Full-Stack-Foundations/stargazers">
          53
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/star" class="js-toggler-form unstarred js-star-button" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="puqwMNE15mlp4qLRwZpFW7tp/K5ksoi0fzEcEBJpL4BM/RQsR+ixs9HQ4+YpXRif681tSAuKdR+StDNhlG+8gg==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star lobrown/Full-Stack-Foundations"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star "></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/lobrown/Full-Stack-Foundations/stargazers">
          53
        </a>
</form>  </div>

  </li>

  <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/fork" class="btn-with-count" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="q2MFtkiB0xG6Zel1Oxs07SIKIWZbwGDPoZAo+UM+4lujHkYRVee4dCqZrB+3Wdi+qpnZ7kIJ2zRSxAnG+MI6rg==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of lobrown/Full-Stack-Foundations to your account"
                aria-label="Fork your own copy of lobrown/Full-Stack-Foundations to your account">
              <span class="octicon octicon-repo-forked "></span>
              Fork
            </button>
</form>
    <a href="/lobrown/Full-Stack-Foundations/network" class="social-count">
      271
    </a>
  </li>
</ul>

    <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public ">
  <span class="octicon octicon-repo "></span>
  <span class="author"><a href="/lobrown" class="url fn" itemprop="url" rel="author"><span itemprop="title">lobrown</span></a></span><!--
--><span class="path-divider">/</span><!--
--><strong><a href="/lobrown/Full-Stack-Foundations" data-pjax="#js-repo-pjax-container">Full-Stack-Foundations</a></strong>

  <span class="page-context-loader">
    <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
  </span>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <a href="/lobrown/Full-Stack-Foundations" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /lobrown/Full-Stack-Foundations">
    <span class="octicon octicon-code "></span>
    Code
</a>
    <a href="/lobrown/Full-Stack-Foundations/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /lobrown/Full-Stack-Foundations/issues">
      <span class="octicon octicon-issue-opened "></span>
      Issues
      <span class="counter">9</span>
</a>
  <a href="/lobrown/Full-Stack-Foundations/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /lobrown/Full-Stack-Foundations/pulls">
    <span class="octicon octicon-git-pull-request "></span>
    Pull requests
    <span class="counter">5</span>
</a>
    <a href="/lobrown/Full-Stack-Foundations/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /lobrown/Full-Stack-Foundations/wiki">
      <span class="octicon octicon-book "></span>
      Wiki
</a>
  <a href="/lobrown/Full-Stack-Foundations/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /lobrown/Full-Stack-Foundations/pulse">
    <span class="octicon octicon-pulse "></span>
    Pulse
</a>
  <a href="/lobrown/Full-Stack-Foundations/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /lobrown/Full-Stack-Foundations/graphs">
    <span class="octicon octicon-graph "></span>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/lobrown/Full-Stack-Foundations/blob/d9cbad3d6a0e0923c16c7824eb8c91ec3e95e709/Lesson_1/lotsofmenus.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:04696818ccf84d6d8b406f5744e1d65d -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title="master"
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span aria-label="Close" class="octicon octicon-x js-menu-close" role="button"></span>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/lobrown/Full-Stack-Foundations/blob/master/Lesson_1/lotsofmenus.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/lobrown/Full-Stack-Foundations/blob/patch-2/Lesson_1/lotsofmenus.py"
               data-name="patch-2"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="patch-2">
                patch-2
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/lobrown/Full-Stack-Foundations/find/master"
          class="js-show-file-finder btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/lobrown/Full-Stack-Foundations" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">Full-Stack-Foundations</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/lobrown/Full-Stack-Foundations/tree/master/Lesson_1" class="" data-branch="master" data-pjax="true" itemscope="url"><span itemprop="title">Lesson_1</span></a></span><span class="separator">/</span><strong class="final-path">lotsofmenus.py</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="right">
        <a class="commit-tease-sha" href="/lobrown/Full-Stack-Foundations/commit/4fe1e0b6a9a3d2a4aa999cf1d91e077539174b8d" data-pjax>
          4fe1e0b
        </a>
        <time datetime="2015-05-05T17:40:24Z" is="relative-time">May 5, 2015</time>
      </span>
      <div>
        <img alt="@lobrown" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/9041401?v=3&amp;s=40" width="20" />
        <a href="/lobrown" class="user-mention" rel="author">lobrown</a>
          <a href="/lobrown/Full-Stack-Foundations/commit/4fe1e0b6a9a3d2a4aa999cf1d91e077539174b8d" class="message" data-pjax="true" title="Made modification to make code PEP8 compliant">Made modification to make code PEP8 compliant</a>
      </div>

    <div class="commit-tease-contributors">
      <a class="muted-link contributors-toggle" href="#blob_contributors_box" rel="facebox">
        <strong>1</strong>
         contributor
      </a>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@lobrown" height="24" src="https://avatars0.githubusercontent.com/u/9041401?v=3&amp;s=48" width="24" />
            <a href="/lobrown">lobrown</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/lobrown/Full-Stack-Foundations/raw/master/Lesson_1/lotsofmenus.py" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/lobrown/Full-Stack-Foundations/blame/master/Lesson_1/lotsofmenus.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/lobrown/Full-Stack-Foundations/commits/master/Lesson_1/lotsofmenus.py" class="btn btn-sm " rel="nofollow">History</a>
    </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/lobrown/Full-Stack-Foundations?branch=master&amp;filepath=Lesson_1%2Flotsofmenus.py"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <span class="octicon octicon-device-desktop "></span>
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/edit/master/Lesson_1/lotsofmenus.py" class="inline-form js-update-url-with-hash" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="gWLB8AqJ2sjf7gSIDl/59Ta/d5+R+Wy9BXVBKfnCFb+ADAfITb4EJ5LZAxrkvrSfyxkof1wodUNwZfmrhDAi+Q==" /></div>
          <button class="octicon-btn tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
            <span class="octicon octicon-pencil "></span>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/lobrown/Full-Stack-Foundations/delete/master/Lesson_1/lotsofmenus.py" class="inline-form" data-form-nonce="33cefdc1406c4a380e0f61d27043bd844daf6fb5" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ZSQmltRvqbZLpZ8D/ygR2a0yOigZtMlILylk1lOuvBZTO90aSJOqUd7u3EWxtUOqPPBSum2zgVg4Q9MGkMXQVg==" /></div>
          <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <span class="octicon octicon-trashcan "></span>
          </button>
</form>  </div>

  <div class="file-info">
      381 lines (244 sloc)
      <span class="file-info-divider"></span>
    14.1 KB
  </div>
</div>

  

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sqlalchemy <span class="pl-k">import</span> create_engine</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> sqlalchemy.orm <span class="pl-k">import</span> sessionmaker</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> database_setup <span class="pl-k">import</span> Restaurant, Base, MenuItem</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">engine <span class="pl-k">=</span> create_engine(<span class="pl-s"><span class="pl-pds">&#39;</span>sqlite:///restaurantmenu.db<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Bind the engine to the metadata of the Base class so that the</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># declaratives can be accessed through a DBSession instance</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">Base.metadata.bind <span class="pl-k">=</span> engine</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">DBSession <span class="pl-k">=</span> sessionmaker(<span class="pl-smi">bind</span><span class="pl-k">=</span>engine)</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># A DBSession() instance establishes all conversations with the database</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># and represents a &quot;staging zone&quot; for all the objects loaded into the</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># database session object. Any change made against the objects in the</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># session won&#39;t be persisted into the database until you call</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># session.commit(). If you&#39;re not happy about the changes, you can</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># revert all of them back to the last commit by calling</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># session.rollback()</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">session <span class="pl-k">=</span> DBSession()</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for UrbanBurger</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Urban Burger<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled veggie patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>French Fries<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>with garlic and parmesan<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$2.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled chicken patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$5.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chocolate Cake<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>fresh baked and served with ice cream<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$3.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Sirloin Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Made with grade A beef<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">menuItem5 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Root Beer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>16oz of refreshing goodness<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$1.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Beverage<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">session.add(menuItem5)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">menuItem6 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Iced Tea<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>with Lemon<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Beverage<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">session.add(menuItem6)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">menuItem7 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Grilled Cheese Sandwich<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>On texas toast with American Cheese<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$3.49<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">session.add(menuItem7)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">menuItem8 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Made with freshest of ingredients and home grown spices<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$5.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">session.add(menuItem8)</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Super Stir Fry</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">restaurant2 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Super Stir Fry<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">session.add(restaurant2)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken Stir Fry<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>With your choice of noodles vegetables and sauces<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    <span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Peking Duck<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span> A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$25<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Spicy Tuna Roll<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce <span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>15<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Nepali Momo <span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Steamed dumplings made with vegetables, spices and meat. <span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>12<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">menuItem5 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Beef Noodle Soup<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>14<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">session.add(menuItem5)</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">menuItem6 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Ramen<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>12<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant2)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">session.add(menuItem6)</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Panda Garden</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Panda Garden<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Pho<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$8.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chinese Dumplings<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Gyoza<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$9.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Stinky Tofu<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Taiwanese dish, deep fried fermented tofu served with pickled cabbage.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled veggie patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$9.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Thyme for that</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Thyme for That Vegetarian Cuisine <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Tres Leches Cake<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$2.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Mushroom risotto<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Portabello mushrooms in a creamy risotto<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$5.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Honey Boba Shaved Snow<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$4.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cauliflower Manchurian<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger &amp; green onions<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">menuItem5 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Aloo Gobi Burrito<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">session.add(menuItem5)</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled veggie patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.80<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Tony&#39;s Bistro</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Tony<span class="pl-cce">\&#39;</span>s Bistro <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Shellfish Tower<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$13.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken and Rice<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken... and rice<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$4.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Mom&#39;s Spaghetti<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Spaghetti with some incredible tomato sauce made by mom<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Choc Full O<span class="pl-cce">\&#39;</span> Mint (Smitten<span class="pl-cce">\&#39;</span>s Fresh Mint Chip ice cream)<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Milk, cream, salt, ..., Liquid nitrogen magic<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$3.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">menuItem5 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Tonkatsu Ramen<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Noodles in a delicious pork-based broth with a soft-boiled egg<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">session.add(menuItem5)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Andala&#39;s</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Andala<span class="pl-cce">\&#39;</span>s<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Lamb Curry<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$9.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken Marsala<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken cooked in Marsala wine sauce with mushrooms<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Potstickers<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Delicious chicken and veggies encapsulated in fried dough.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Nigiri Sampler<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Maguro, Sake, Hamachi, Unagi, Uni, TORO!<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.75<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled veggie patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.00<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Auntie Ann&#39;s</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Auntie Ann<span class="pl-cce">\&#39;</span>s Diner&#39; <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">menuItem9 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken Fried Steak<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Fresh battered sirloin steak fried and smothered with cream gravy<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$8.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">session.add(menuItem9)</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Boysenberry Sorbet<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$2.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Broiled salmon<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Salmon fillet marinated with fresh herbs and broiled hot &amp; fast<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$10.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">menuItem3 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Morels on toast (seasonal)<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Wild morel mushrooms fried in butter, served on herbed toast slices<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">session.add(menuItem3)</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">menuItem4 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Tandoori Chicken<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$8.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">session.add(menuItem4)</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Veggie Burger<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Juicy grilled veggie patty with tomato mayo and lettuce<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$9.50<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">menuItem10 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Spinach Ice Cream<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>vanilla ice cream made with organic spinach leaves<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">                      <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$1.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">session.add(menuItem10)</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Menu for Cocina Y Amor</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cocina Y Amor <span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Super Burrito Al Pastor<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$5.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">menuItem2 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Cachapa<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. <span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$7.99<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Entree<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">session.add(menuItem2)</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">restaurant1 <span class="pl-k">=</span> Restaurant(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>State Bird Provisions<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">session.add(restaurant1)</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Chantrelle Toast<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$5.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appetizer<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">session.commit</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Guanciale Chawanmushi<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$6.95<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">menuItem1 <span class="pl-k">=</span> MenuItem(<span class="pl-smi">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Lemon Curd Ice Cream Sandwich<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">                     <span class="pl-smi">price</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>$4.25<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">course</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Dessert<span class="pl-pds">&quot;</span></span>, <span class="pl-smi">restaurant</span><span class="pl-k">=</span>restaurant1)</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">session.add(menuItem1)</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">session.commit()</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line"><span class="pl-k">print</span> <span class="pl-s"><span class="pl-pds">&quot;</span>added menu items!<span class="pl-pds">&quot;</span></span></td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>

    </div>
  </div>

    </div>

        <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://github.com/pricing" data-ga-click="Footer, go to pricing, text:pricing">Pricing</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github " title="GitHub "></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.08921s from github-fe128-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <span class="octicon octicon-x"></span>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" integrity="sha256-7460qJ7p88i3YTMH/liaj1cFgX987ie+xRzl6WMjSr8=" src="https://assets-cdn.github.com/assets/frameworks-ef8eb4a89ee9f3c8b7613307fe589a8f5705817f7cee27bec51ce5e963234abf.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-S2uOfRHrt7zoUSbTtBMMgAQfKubV1u+JAajAw/fLgNI=" src="https://assets-cdn.github.com/assets/github-4b6b8e7d11ebb7bce85126d3b4130c80041f2ae6d5d6ef8901a8c0c3f7cb80d2.js"></script>
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>

