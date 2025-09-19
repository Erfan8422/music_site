(function($) {

    initSinglePlayer();
    
    function initSinglePlayer() {
        const players = $('.jplayer');
        players.each(function(index) {
            const player = $(this);
            const ancestor = player.data('ancestor');
            const songUrl = player.data('url');
            player.jPlayer({
                ready: function () {
                    $(this).jPlayer("setMedia", {
                        mp3: songUrl
                    });
                },
                play: function() { // To avoid multiple jPlayers playing together.
                    $(this).jPlayer("pauseOthers");
                    try {
                        wavesurfer.pause();
                    } catch(err) {
                        console.error(err);
                    }
                },
                swfPath: "jPlayer",
                supplied: "mp3",
                cssSelectorAncestor: ancestor,
                wmode: "window",
                globalVolume: false,
                useStateClassSkin: true,
                autoBlur: false,
                smoothPlayBar: true,
                keyEnabled: true,
                solution: 'html',
                preload: 'metadata',
                volume: 0.8,
                muted: false,
                backgroundColor: '#000000',
                errorAlerts: false,
                warningAlerts: false
            });
        });
    }

    function currentTimeAlign() {
        $('.jp-progress').each(function() {
            const jpPBarW = $(this).find('.jp-play-bar').innerWidth();
            if (jpPBarW > 40) {
                $(this).addClass('middle');
            } else {
                $(this).removeClass('middle');
            }
        });
    }
    const intervalId = setInterval(currentTimeAlign, 10);

    $('.single_player').each(function() {
        let rwaction;
        const thisItem = $(this);
        const player = thisItem.find('.jplayer');

        thisItem.find('.jp-next').click(function() { 
            FastforwardTrack();
        });

        thisItem.find('.jp-prev').click(function() { 
            RewindTrack();
        });

        function GetPlayerProgress() {
            return (thisItem.find('.jp-play-bar').width() / $('.jp-seek-bar').width() * 100);
        }

        function RewindTrack() {
            const currentProgress = GetPlayerProgress();
            const futureProgress = currentProgress - 5;
            if (futureProgress <= 0) {
                clearInterval(rwaction);
                player.jPlayer("pause", 0);
            } else {
                player.jPlayer("playHead", parseInt(futureProgress, 10));
            }
        }

        function FastforwardTrack() {
            const currentProgress = GetPlayerProgress();
            const futureProgress = currentProgress + 5;
            if (futureProgress >= 100) {
                clearInterval(ffaction);
                player.jPlayer("playHead", parseInt($('.jp-duration').text().replace(':', '')));
            } else {
                player.jPlayer("playHead", parseInt(futureProgress, 10));
            }
        }
    });

})(jQuery);



