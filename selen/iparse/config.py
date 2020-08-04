GRAPHQL_URL = "https://www.instagram.com/graphql/query/"
BRIEF_PROFILE_INFO_URL = "https://www.instagram.com/{0}/?__a=1"

USER_PROFILE_HASH = "15bf78a4ad24e33cbd838fdb31353ac1"
USER_FOLLOWERS_HASH = "c76146de99bb02f6415203be841dd25a"
MEDIA_LIKERS_HASH = "d5d763b1e2acf209d62d22d184488e57"

USER_PROFILE_VARIABLES = "{{\"id\":\"{0}\",\"first\":{1}}}"
USER_PROFILE_VARIABLES_CURSOR = "{{\"id\":\"{0}\",\"first\":{1},\"after\":\"{2}\"}}"
USER_FOLLOWERS_VARIABLES = "{{\"id\":\"{0}\",\"include_reel\":true,\"fetch_mutual\":true,\"first\":{1}}}"
USER_FOLLOWERS_VARIABLES_CURSOR = "{{\"id\":\"{0}\",\"include_reel\":true,\"fetch_mutual\":true,\"first\":{1},\"after\":\"{2}\"}}"
MEDIA_LIKERS_VARIABLES = "{{\"shortcode\":\"{0}\",\"include_reel\":true,\"first\":{1}}}"
MEDIA_LIKERS_VARIABLES_CURSOR = "{{\"shortcode\":\"{0}\",\"include_reel\":true,\"first\":{1},\"after\":\"{2}\"}}"
