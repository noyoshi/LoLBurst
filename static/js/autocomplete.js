/*
$(document).ready(function(){
    var json = $.getJSON("../../item_icons.json");
    $('#autocomplete-input-champ').autocomplete({
        data: json,
        limit: 10,
        minLength: 1
    });
});
$(document).ready(function(){
    var json = $.getJSON("../../item_icons.json");
    $('#autocomplete-input-item').autocomplete({

        data: json,
        limit: 10,
        minLength: 1
    });
});
*/

$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
});



$(document).ready(function(){
    $('#autocomplete-input-champ').autocomplete({
        data: {"Yorick": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Yorick.png", "Vayne": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Vayne.png", "Vel'Koz": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Velkoz.png", "Lucian": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Lucian.png", "Vi": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Vi.png", "Aurelion Sol": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/AurelionSol.png", "Kindred": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kindred.png", "Rakan": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Rakan.png", "Lissandra": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Lissandra.png", "Singed": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Singed.png", "Nami": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nami.png", "Ezreal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ezreal.png", "Varus": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Varus.png", "Hecarim": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Hecarim.png", "Alistar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Alistar.png", "Malphite": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Malphite.png", "Ivern": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ivern.png", "Maokai": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Maokai.png", "Akali": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Akali.png", "Darius": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Darius.png", "Fizz": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Fizz.png", "Taliyah": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Taliyah.png", "Ahri": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ahri.png", "Kha'Zix": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Khazix.png", "Rumble": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Rumble.png", "Zed": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Zed.png", "Ziggs": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ziggs.png", "Skarner": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Skarner.png", "Sion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Sion.png", "Evelynn": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Evelynn.png", "Azir": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Azir.png", "Anivia": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Anivia.png", "Volibear": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Volibear.png", "Sona": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Sona.png", "Lulu": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Lulu.png", "Poppy": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Poppy.png", "Talon": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Talon.png", "Ashe": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ashe.png", "Graves": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Graves.png", "Tryndamere": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Tryndamere.png", "Jax": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Jax.png", "Thresh": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Thresh.png", "Kennen": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kennen.png", "Kassadin": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kassadin.png", "Fiora": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Fiora.png", "Galio": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Galio.png", "Tristana": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Tristana.png", "Xayah": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Xayah.png", "Pantheon": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Pantheon.png", "Kayn": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kayn.png", "Viktor": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Viktor.png", "Janna": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Janna.png", "Jhin": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Jhin.png", "Nasus": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nasus.png", "Karthus": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Karthus.png", "Kayle": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kayle.png", "Rek'Sai": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/RekSai.png", "Annie": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Annie.png", "Cassiopeia": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Cassiopeia.png", "Heimerdinger": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Heimerdinger.png", "Zoe": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Zoe.png", "Soraka": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Soraka.png", "Taric": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Taric.png", "Cho'Gath": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Chogath.png", "Swain": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Swain.png", "Kalista": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kalista.png", "Xerath": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Xerath.png", "Fiddlesticks": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Fiddlesticks.png", "Brand": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Brand.png", "Aatrox": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Aatrox.png", "Quinn": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Quinn.png", "Blitzcrank": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Blitzcrank.png", "Draven": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Draven.png", "Caitlyn": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Caitlyn.png", "Syndra": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Syndra.png", "Twisted Fate": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/TwistedFate.png", "Illaoi": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Illaoi.png", "Dr. Mundo": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/DrMundo.png", "Jinx": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Jinx.png", "Lee Sin": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/LeeSin.png", "Lux": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Lux.png", "Ryze": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ryze.png", "Olaf": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Olaf.png", "Kled": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kled.png", "Zyra": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Zyra.png", "Bard": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Bard.png", "Orianna": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Orianna.png", "Amumu": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Amumu.png", "Urgot": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Urgot.png", "Nunu": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nunu.png", "Teemo": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Teemo.png", "Irelia": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Irelia.png", "Camille": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Camille.png", "Nidalee": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nidalee.png", "Gragas": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Gragas.png", "Kog'Maw": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/KogMaw.png", "Shaco": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Shaco.png", "Jayce": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Jayce.png", "Gangplank": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Gangplank.png", "Riven": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Riven.png", "Veigar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Veigar.png", "Jarvan IV": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/JarvanIV.png", "Yasuo": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Yasuo.png", "Corki": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Corki.png", "Xin Zhao": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/XinZhao.png", "Vladimir": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Vladimir.png", "Ornn": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ornn.png", "Nocturne": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nocturne.png", "Wukong": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/MonkeyKing.png", "Elise": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Elise.png", "Garen": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Garen.png", "Udyr": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Udyr.png", "Leona": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Leona.png", "Ekko": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Ekko.png", "Braum": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Braum.png", "Gnar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Gnar.png", "Twitch": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Twitch.png", "Renekton": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Renekton.png", "Trundle": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Trundle.png", "Sivir": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Sivir.png", "Rammus": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Rammus.png", "Shyvana": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Shyvana.png", "Tahm Kench": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/TahmKench.png", "Mordekaiser": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Mordekaiser.png", "Rengar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Rengar.png", "Nautilus": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Nautilus.png", "Malzahar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Malzahar.png", "Morgana": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Morgana.png", "Miss Fortune": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/MissFortune.png", "Zilean": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Zilean.png", "Kai'Sa": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Kaisa.png", "LeBlanc": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Leblanc.png", "Katarina": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Katarina.png", "Warwick": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Warwick.png", "Sejuani": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Sejuani.png", "Diana": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Diana.png", "Shen": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Shen.png", "Karma": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Karma.png", "Zac": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Zac.png", "Master Yi": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/MasterYi.png"
        },
        limit: 10,
        minLength: 1
    });
});

$(document).ready(function(){
    $('#autocomplete-input-item').autocomplete({
        data: {"Enchantment: Cinderhulk": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3672.png", "Sterak's Gage": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3053.png", "Poro-Snax": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2052.png", "Tower: Beam of Ruination": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3634.png", "Minion Dematerializer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2403.png", "Circlet of the Iron Solari": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3383.png", "Phantom Dancer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3046.png", "Salvation": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3382.png", "Slightly Magical Boots": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2422.png", "Muramana": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3042.png", "Liandry's Torment": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3151.png", "Trinity Force": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3078.png", "Tower: Storm Bulwark": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3636.png", "Maw of Malmortius": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3156.png", "Rabadon's Deathcap": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3089.png", "Youmuu's Ghostblade": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3142.png", "Lich Bane": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3100.png", "Giant Slayer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3034.png", "Mortal Reminder": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3033.png", "Hextech Revolver": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3145.png", "Edge of Night": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3814.png", "Infinity Edge": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3031.png", "B. F. Sword": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1038.png", "The Hex Core mk-1": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3196.png", "Remnant of the Aspect": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3401.png", "Banner of Command": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3060.png", "Warmog's Armor": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3083.png", "Prototype Hex Core": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3200.png", "Refillable Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2031.png", "Spellbinder": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3907.png", "Banshee's Veil": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3102.png", "Death's Dance": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3812.png", "Elixir of Iron": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2138.png", "Chain Vest": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1031.png", "Corrupting Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2033.png", "Greater Vision Totem (Trinket)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3362.png", "Quicksilver Sash": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3140.png", "Void Staff": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3135.png", "Remnant of the Watchers": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3092.png", "Forbidden Idol": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3114.png", "Cloth Armor": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1029.png", "Raptor Cloak": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2053.png", "Siege Sight Warder": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3649.png", "Aether Wisp": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3113.png", "Titanic Hydra": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3748.png", "Frostfang": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3098.png", "Morellonomicon": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3165.png", "Executioner's Calling": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3123.png", "Statikk Shiv": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3087.png", "Needlessly Large Rod": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1058.png", "Blade of the Ruined King": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3153.png", "Zeal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3086.png", "Catalyst of Aeons": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3010.png", "Sunfire Cape": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3068.png", "Hextech Protobelt-01": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3152.png", "Twin Shadows": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3905.png", "Pilfered Stealth Ward": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2056.png", "Doran's Ring": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1056.png", "Ravenous Hydra": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3074.png", "Diet Poro-Snax": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2054.png", "Vanguard Banner": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3641.png", "Peering Farsight Ward": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2057.png", "Wit's End": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3091.png", "Siege Teleport (Inactive)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3648.png", "Greater Stealth Totem (Trinket)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3361.png", "Shurelya's Reverie": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2065.png", "Seeker's Armguard": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3191.png", "Commencing Stopwatch": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2419.png", "Bami's Cinder": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3751.png", "Giant's Belt": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1011.png", "Blasting Wand": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1026.png", "Nashor's Tooth": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3115.png", "Abyssal Mask": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3001.png", "Mercurial Scimitar": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3139.png", "Remnant of the Ascended": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3069.png", "Hexdrinker": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3155.png", "Sheen": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3057.png", "Sly Sack of Gold": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2319.png", "Aegis of the Legion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3105.png", "Bilgewater Cutlass": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3144.png", "Looted Biscuit of Rejuvenation": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2012.png", "The Obsidian Cleaver": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3380.png", "The Dark Seal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1082.png", "Amplifying Tome": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1052.png", "Elixir of Wrath": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2140.png", "Vampiric Scepter": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1053.png", "Warding Totem (Trinket)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3340.png", "Shield Totem": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3647.png", "Boots of Swiftness": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3009.png", "Elixir of Sorcery": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2139.png", "Long Sword": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1036.png", "Poacher's Dirk": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3252.png", "Sorcerer's Shoes": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3020.png", "Guinsoo's Rageblade": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3124.png", "Dead Man's Plate": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3742.png", "Control Ward": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2055.png", "Hunter's Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2032.png", "Guardian Angel": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3026.png", "Gargoyle Stoneplate": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3193.png", "Tear of the Goddess (Quick Charge)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3073.png", "Dagger": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1042.png", "Tiamat": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3077.png", "Pilfered Health Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2061.png", "Spellthief's Edge": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3303.png", "Explorer's Ward": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2050.png", "Thornmail": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3075.png", "Doran's Shield": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1054.png", "Farsight Alteration": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3363.png", "Boots of Speed": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1001.png", "Rylai's Crystal Scepter": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3116.png", "Enchantment: Bloodrazor": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1419.png", "Rabadon's Deathcrown": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3374.png", "Pilfered Potion of Rouge": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2062.png", "Iceborn Gauntlet": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3025.png", "Berserker's Greaves": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3006.png", "Zz'Rot Portal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3512.png", "Hextech Gunblade": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3146.png", "Essence Reaver": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3508.png", "Lost Chapter": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3802.png", "Head of Kha'Zix": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3455.png", "Travel Size Elixir of Sorcery": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2059.png", "Zeke's Convergence": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3050.png", "Frozen Mallet": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3022.png", "Manamune": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3004.png", "Faerie Charm": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1004.png", "Ancient Coin": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3301.png", "Total Biscuit of Everlasting Will": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2010.png", "Redemption": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3107.png", "Mercury's Treads": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3111.png", "Enchantment: Warrior": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1412.png", "Hunter's Machete": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1041.png", "Manamune (Quick Charge)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3008.png", "Trinity Fusion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3384.png", "Haunting Guise": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3136.png", "The Hex Core mk-2": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3197.png", "Jaurim's Fist": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3052.png", "Serrated Dirk": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3134.png", "Entropy Field": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3643.png", "Knight's Vow": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3109.png", "Doran's Blade": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1055.png", "Boots of Mobility": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3117.png", "Skirmisher's Sabre": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3715.png", "Infernal Mask": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3379.png", "The Bloodthirster": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3072.png", "Adaptive Helm": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3194.png", "Forgefire Cape": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3373.png", "Fire at Will": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3901.png", "Locket of the Iron Solari": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3190.png", "Recurve Bow": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1043.png", "Spectre's Cowl": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3211.png", "Oblivion Orb": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3916.png", "Ohmwrecker": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3056.png", "Lord Dominik's Regards": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3036.png", "Rod of Ages (Quick Charge)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3029.png", "Rapid Firecannon": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3094.png", "Stopwatch": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2420.png", "Molten Edge": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3371.png", "Kircheis Shard": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2015.png", "Elixir Of Skill": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2011.png", "Targon's Brace": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3097.png", "Mikael's Crucible": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3222.png", "Port Pad": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3635.png", "Enchantment: Runic Echoes": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3673.png", "Sapphire Crystal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1027.png", "Oracle Alteration": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3364.png", "Siege Refund": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3642.png", "Bramble Vest": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3076.png", "Mana Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2004.png", "Sweeping Lens (Trinket)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3341.png", "Siege Ballista": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3631.png", "Death's Daughter": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3902.png", "Archangel's Staff": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3003.png", "Chalice of Harmony": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3028.png", "Rod of Ages": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3027.png", "Negatron Cloak": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1057.png", "Ardent Censer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3504.png", "Frozen Heart": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3110.png", "Pickaxe": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1037.png", "Duskblade of Draktharr": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3147.png", "Relic Shield": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3302.png", "Brawler's Gloves": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1051.png", "Glacial Shroud": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3024.png", "Runaan's Hurricane": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3085.png", "Broken Stopwatch": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2421.png", "Zhonya's Paradox": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3386.png", "Null-Magic Mantle": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1033.png", "Flash Zone": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3640.png", "Athene's Unholy Grail": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3174.png", "Stalker's Blade": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3706.png", "Hunter's Talisman": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1039.png", "Righteous Glory": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3800.png", "Phage": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3044.png", "Warden's Mail": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3082.png", "Total Biscuit of Rejuvenation": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2009.png", "Caulfield's Warhammer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3133.png", "Perfect Hex Core": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3198.png", "Last Whisper": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3035.png", "Cloak of Agility": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1018.png", "Fiendish Codex": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3108.png", "Nomad's Medallion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3096.png", "Mejai's Soulstealer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3041.png", "Ruby Crystal": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1028.png", "Rejuvenation Bead": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1006.png", "Travel Size Elixir of Wrath": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2060.png", "Health Potion": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2003.png", "The Black Spear": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3599.png", "Ionian Boots of Lucidity": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3158.png", "Archangel's Staff (Quick Charge)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3007.png", "Zhonya's Hourglass": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3157.png", "Seer Stone (Trinket)": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3645.png", "Travel Size Elixir of Iron": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/2058.png", "Kindlegem": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3067.png", "Raise Morale": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3903.png", "Hextech GLP-800": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3030.png", "Cull": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1083.png", "Randuin's Omen": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3143.png", "Crystalline Bracer": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3801.png", "Spirit Visage": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3065.png", "Ninja Tabi": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3047.png", "The Black Cleaver": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3071.png", "Luden's Echo": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3285.png", "Stinger": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3101.png", "Tear of the Goddess": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3070.png", "Seraph's Embrace": "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/3048.png"
        },
        limit: 10,
        minLength: 1
    });
});
